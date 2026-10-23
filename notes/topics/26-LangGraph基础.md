---
title: LangGraph 基础
category: 工程
keywords: [LangGraph, State, Node, Edge, 条件边, 循环, StateGraph, checkpointer, Agent 循环]
dates: [2026-10-23]
---

# LangGraph 基础

> 一句话：**LangGraph = 把 Agent 的循环画成一张图**——State 是流动的数据，Node 是做事，Edge 是走向。

## 1. 为什么需要 LangGraph

`create_react_agent(llm, tools)` 一行就能得到 Agent，但它是个**黑盒**。
当你想让 Agent：

- 走**分支**（不同类型问题走不同流程）
- 中途**停下来等人确认**
- 记住**多轮历史**
- 多个 agent **分工协作**

就需要自己搭图——这就是 LangGraph。

## 2. 四个核心概念

| 概念 | 是什么 | 类比 |
| --- | --- | --- |
| **State** | 图里流动的数据（通常是消息列表） | 传送带上的货物 |
| **Node** | 一个函数，读 State、返回更新 | 工位（加工一下） |
| **Edge** | 固定连线：A 之后一定走 B | 传送带 |
| **Conditional Edge** | 按条件决定走哪条 | 岔路口的调度员 |

## 3. 最小可用模板

```python
from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


# ① State：流动的数据
class AgentState(TypedDict):
    # Annotated + add_messages = "新消息追加到列表"，而不是覆盖
    messages: Annotated[list[AnyMessage], add_messages]


# ② 工具
@tool
def add(a: int, b: int) -> int:
    """计算两个整数之和。"""
    return a + b


TOOLS = [add]
llm = get_llm(temperature=0).bind_tools(TOOLS)   # 绑定工具


# ③ Node：调用模型
def agent_node(state: AgentState) -> dict:
    return {"messages": [llm.invoke(state["messages"])]}


# ④ 条件边：继续还是结束
def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"     # 要调工具
    return END             # 答完了


# ⑤ 建图
g = StateGraph(AgentState)
g.add_node("agent", agent_node)
g.add_node("tools", ToolNode(TOOLS))
g.add_edge(START, "agent")
g.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
g.add_edge("tools", "agent")      # ← 这一条形成循环
app = g.compile()
```

## 4. 图长什么样

```
START → agent ─┬─(有 tool_calls)→ tools ─┐
               │                        │
               └─(没有)→ END            │
                        ↑               │
                        └───────────────┘
                     （tools 执行完回到 agent）
```

## 5. 最关键的一行：`Annotated[list, add_messages]`

```python
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]   # ✅ 追加
```

这就是 **reducer（归约器）** 的概念：

| 写法 | 节点返回新消息时 |
| --- | --- |
| `messages: list` | **覆盖**（历史全丢） |
| `messages: Annotated[list, add_messages]` | **追加**（保留历史） |

> Agent 之所以能"记得上一步的工具结果"，靠的就是这个累加。
> 这是新手最常踩的坑。

## 6. 加了 checkpointer 才有"记忆"

```python
from langgraph.checkpoint.memory import MemorySaver

app = g.compile(checkpointer=MemorySaver())

# 调用时传 thread_id，同一个 id 就是同一个会话
config = {"configurable": {"thread_id": "user-1"}}
app.invoke({"messages": [("user", "我叫小明")]}, config)
app.invoke({"messages": [("user", "我叫什么？")]}, config)   # 它会记得
```

| 概念 | 作用 |
| --- | --- |
| `checkpointer` | 把每一步状态存下来 |
| `thread_id` | 区分不同会话（同一 id = 同一段记忆） |
| `MemorySaver` | 存内存（重启就没了） |
| `SqliteSaver` | 存文件（可持久化） |

## 7. 人工介入（Human-in-the-loop）

在关键步骤（花钱、删数据、发消息）前暂停，等人确认：

```python
from langgraph.types import interrupt, Command

def risky_node(state):
    answer = interrupt("要执行删除操作，确认吗？")   # 暂停，把问题抛给调用方
    if answer != "yes":
        return {"messages": [("ai", "已取消")]}
    ...
```

## 8. 高级控制流（学到后期再看）

| 能力 | 用途 |
| --- | --- |
| **Subgraph** | 把复杂流程拆成子图，像函数一样复用 |
| **Send API** | 动态并行分支（map-reduce） |
| **stream_mode** | 流式看每一步的输出（调试神器） |
| **recursion_limit** | 防止死循环的上限 |

## ⚠️ 易错点速记

1. **State 字段忘了 `Annotated[..., add_messages]`** → 历史消息被覆盖，Agent 失忆
2. **条件边没有返回 `END`** → 死循环，报递归超限
3. **节点返回值必须是 dict**（要合并进 State 的键）
4. **`compile()` 别忘**，图不编译不能用
5. **没有 `checkpointer` + `thread_id`** → 多轮对话记不住
6. **`ToolNode` 要传工具列表**，不是单个工具
7. 模型不绑定工具（`bind_tools`）就不会产生 `tool_calls`，循环永远走得通但没用

## 🔗 关联

- Agent 环境与 DeepSeek → [24-Agent开发环境与DeepSeek](24-Agent开发环境与DeepSeek.md)
- Langflow 对照 → [25-Langflow基础操作](25-Langflow基础操作.md)
- 工具定义（装饰器）→ [18-闭包](18-闭包.md)
- 长篇规划 → [LangChain + LangGraph 完全掌握路线](../plans/2026-10-23-LangChain-LangGraph掌握路线.md)
- 实践脚本 → `agent-lab/05_langgraph_agent.py`
