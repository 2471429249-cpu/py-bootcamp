---
title: Agent 开发环境与 DeepSeek 接入
category: 工程
keywords: [Agent, LangChain, LangGraph, DeepSeek, langchain-openai, base_url, OpenAI 兼容, venv, 环境]
dates: [2026-10-22]
---

# Agent 开发环境与 DeepSeek 接入

> 一句话：**DeepSeek 的 API 是 OpenAI 完全兼容的**，所以用官方 `langchain-openai` 改个 `base_url` 就能连——**一个第三方插件都不需要装**。

## 1. 核心认知：为什么不需要"DeepSeek 插件"

DeepSeek 的接口格式和 OpenAI 一模一样（都是 `/chat/completions`），所以：

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key="sk-xxx",
    base_url="https://api.deepseek.com",   # ← 只改这一个参数
)
resp = llm.invoke("你好")
```

> ⚠️ **安全提醒**：网上那些"DeepSeek 插件/扩展"，很多是木马重灾区。
> **官方组件 + 自定义 base_url** 才是正确做法，全程零第三方代码。

## 2. 本机环境（agent-lab）

| 项 | 值 |
| --- | --- |
| 位置 | `桌面\agent-lab\` |
| Python | 3.13.7（独立 venv，不影响 Anaconda） |
| langchain | 1.4.7 |
| langchain-core | 1.6.13 |
| langchain-openai | 1.7.2 |
| langgraph | 1.2.16 |
| pydantic | 2.14.1 |

**为什么用独立 venv**：不污染系统 Python / Anaconda，删掉文件夹就等于完全卸载。

### 项目结构

```
agent-lab/
├── .env              ← 唯一要改的地方（填 API Key）
├── config.py         ← 统一配置：读 .env、返回 DeepSeek 客户端
├── 00_check.py       ← 环境自检（依赖 + Key + 真实调用）
├── 01_hello_llm.py   ← 第一次调用模型
├── 02_chain.py       ← LCEL 管道：提示词 | 模型 | 解析器
├── 03_tool_agent.py  ← 工具调用 Agent（ReAct 循环）
├── requirements.txt
├── run.bat           ← 一键运行（自动用 venv）
└── README.md         ← 完整学习路线
```

## 3. 配置方式：只改一个文件

`.env`：

```ini
DEEPSEEK_API_KEY=sk-你的key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

代码里用 `python-dotenv` 读取，避免把 key 写进代码（也避免提交到 Git）：

```python
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")
```

> `.env` 必须写进 `.gitignore`，**密钥永远不进版本库**。

## 4. 模型名怎么选

| 模型名 | 用途 |
| --- | --- |
| `deepseek-chat` | 通用对话（V3 系列），日常用这个 |
| `deepseek-reasoner` | 推理模型（R1 系列），复杂推理用，更慢更贵 |

## 5. Langflow 里怎么接（两条路）

### 路线 A：原生 DeepSeek 组件（更简单）

Langflow 1.12 自带 **`DeepSeek`** 组件，字段：

| 字段 | 填什么 |
| --- | --- |
| **DeepSeek API 密钥** | 你的 key |
| **DeepSeek API 基础** | 默认 `https://api.deepseek.com`，不用改 |
| **型号名称** | `deepseek-chat` |

### 路线 B：OpenAI Compatible 提供者

Langflow 1.12 内置官方提供者 **`OpenAI Compatible`**（来自官方包 `lfx-openai-compatible`）：

| 字段 | 填什么 |
| --- | --- |
| **Base URL** | `https://api.deepseek.com`（**不要**加 `/v1`，组件会自动补） |
| **API Key** | 你的 key |
| **Model** | 从下拉里选 `deepseek-chat`（它会请求 `/v1/models` 实时拉取） |

> 两条路都**不需要任何第三方插件**。

## 6. ⚠️ 一个必须先知道的限制：DeepSeek 没有 embedding 接口

做 **RAG**（检索增强生成）时，"把文档变成向量"这一步需要 **embedding 模型**，而 DeepSeek 官方**不提供**。
三种替代方案：

| 方案 | 说明 |
| --- | --- |
| 本地 `sentence-transformers` | 如 `BAAI/bge-small-zh-v1.5`，免费、离线、推荐 |
| Ollama 本地 embedding 模型 | 便于统一管理 |
| 其他厂商的 embedding API | 如硅基流动 |

> 所以 RAG 依赖**暂时没装**，等学到那一步再按需装。

## 7. Agent 开发全流程（7 阶段）

```
① 调用模型        invoke / stream                 ← 当前进度
② 提示词工程      PromptTemplate / few-shot
③ 结构化输出      Pydantic + with_structured_output
④ 工具调用        @tool + bind_tools
⑤ Agent 循环      LangGraph 状态图   ★核心
⑥ RAG            切分 → 向量化 → 检索 → 拼提示词
⑦ 工程化          日志 / trace / 评估 / 部署
```

### 关键 API 速查

```python
llm.invoke("文本")                  # 同步调用
llm.stream("文本")                  # 流式（同步，for 循环取）
llm.with_structured_output(Model)   # 结构化输出
llm.bind_tools([t1, t2])            # 绑定工具

prompt = ChatPromptTemplate.from_messages([("system", "..."), ("human", "{q}")])
chain = prompt | llm | StrOutputParser()

@tool
def my_tool(x: int) -> int:
    """工具说明（docstring 会被模型看到，必须写清楚）"""
    return x
```

> **不需要 async**：LangChain 的同步 API（`invoke`/`stream`）完全够用。

## 8. ⚠️ DeepSeek 的「兼容性边界」（实测踩过的坑）

DeepSeek 说"OpenAI 兼容"，但**是部分兼容**。实测结果：

| 能力 | 支持 |
| --- | --- |
| 普通对话 `/chat/completions` | ✅ |
| 函数调用（function calling） | ✅ |
| `response_format: json_object` | ✅ |
| **`response_format: json_schema`** | ❌ **不支持** |
| embedding 接口 | ❌ 没有 |

**踩坑现场**：`llm.with_structured_output(Movie)` 报
`This response_format type is unavailable now`。

**原因**：新版 langchain 的 `with_structured_output` **默认发 `json_schema`**。

**修复**：

```python
structured = llm.with_structured_output(Movie, method="function_calling")
```

| method | 原理 | DeepSeek |
| --- | --- | --- |
| `json_schema` | 直接要求按 schema 返回 | ❌ |
| `json_mode` | 返回 JSON 文本自行解析 | ✅（需额外提示） |
| **`function_calling`** | 把结构伪装成"调用函数" | ✅ **推荐** |

> **经验总结**：「OpenAI 兼容」≠「100% 兼容」。遇到报错先看它**具体**说哪项不支持，再换等价实现。
> 通义、Kimi、智谱等国产模型也有类似差异。

## ⚠️ 易错点速记

1. `base_url` 写成 `https://api.deepseek.com/v1` 再让组件补 `/v1` → 变成 `/v1/v1`，报错
2. 模型名写错（DeepSeek 只有 `deepseek-chat` / `deepseek-reasoner`）
3. key 前后有空格 → 401
4. `.env` 提交进 Git → 密钥泄露（务必 `.gitignore`）
5. 以为要装"DeepSeek 插件" → 恰恰是最危险的做法
6. 想用 DeepSeek 做 embedding → 它没有，得另找方案
7. `with_structured_output` 忘了 `method="function_calling"` → DeepSeek 报 `json_schema` 不支持

## 🔗 关联

- Langflow 操作 → [25-Langflow基础操作](25-Langflow基础操作.md)
- 类型注解（Pydantic/dataclass 基础）→ [20-类型注解](20-类型注解.md)
- 装饰器（`@tool` 的本质）→ [18-闭包](18-闭包.md)
- 异常处理（API 报错处理）→ [22-异常处理](22-异常处理.md)
