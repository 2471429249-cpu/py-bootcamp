# LangChain + LangGraph 完全掌握路线（项目集导向）

> 建立日期：2026-10-23
> 目标：**完全掌握 LangChain + LangGraph**，并沉淀出一套能写进简历的 **Agent 项目集**。
> 节奏：每天 2~3 小时，总计约 **12~14 周**。
> 环境：`桌面\agent-lab\`（独立 venv，Python 3.13.7）

---

## 一、总览：7 个阶段

```
阶段 0  基础打通        ✅ 已完成（调用模型 / 提示词 / 结构化输出 / 工具 / LangGraph 首图）
阶段 1  LangChain 核心      1.5 周
阶段 2  工具与 Agent        1 周
阶段 3  LangGraph 深入 ★    2.5 周
阶段 4  RAG                 2.5 周
阶段 5  工程化与部署        2 周
阶段 6  高级模式            2 周
阶段 7  项目集整合          2.5 周
```

**主线逻辑**：先会用（0→2）→ 会搭循环（3）→ 会接知识（4）→ 会交付（5）→ 会复杂系统（6）→ 会包装成作品（7）。

---

## 二、阶段 0：基础打通（已完成 ✅）

| 已掌握 | 对应文件 |
|---|---|
| 调用大模型（`invoke`） | `01_hello_llm.py` |
| LCEL 管道（提示词 \| 模型 \| 解析器） | `02_chain.py` |
| 工具调用 Agent（`@tool` + ReAct 循环） | `03_tool_agent.py` |
| 结构化输出（Pydantic + `with_structured_output`） | `04_structured.py` |
| LangGraph 手动建图（State/Node/Edge/条件边） | `05_langgraph_agent.py`（**待跑通**） |
| Langflow 可视化（三个入门流程） | Langflow 桌面版 |

**遗留问题**：`05_langgraph_agent.py` 尚未跑通 → 阶段 3 开头第一件事就是解决它。

---

## 三、阶段 1：LangChain 核心（约 1.5 周）

### 要掌握的知识

**1. 消息体系（Messages）**
- `SystemMessage` / `HumanMessage` / `AIMessage` / `ToolMessage` 四种角色
- `AIMessage.tool_calls`、`tool_call_id` 的作用（工具结果要与调用配对的机制）
- 消息列表如何构成一次对话

**2. 提示词进阶**
- `ChatPromptTemplate`、`MessagesPlaceholder`（插入历史）
- f-string 变量、部分变量（`.partial()`）
- few-shot 示例的正确写法

**3. 输出解析**
- `StrOutputParser` / `JsonOutputParser` / `PydanticOutputParser`
- `with_structured_output` 的三种 method（`json_schema` / `json_mode` / `function_calling`）

**4. LCEL 深入**
- `invoke` / `batch` / `stream` 三种调用
- `RunnablePassthrough`（原样传递）、`RunnableLambda`（包装普通函数）
- `RunnableParallel`（并行分支）、`|` 的组合语义
- `RunnableConfig`（传 config、回调、标签）

**5. 回调与日志**
- `callbacks` 抓取 token 用量、耗时
- 何时用 LangSmith（后面阶段 5 再深入）

### 产出（验收）

- [ ] 写一个**多步骤文本处理流水线**：输入一段文章 → 提取要点 → 生成摘要 → 输出 markdown
- [ ] 全程用 LCEL 拼接，至少用到 `RunnableParallel` 和 `RunnablePassthrough`
- [ ] 能打印每次调用的 token 用量

### 检验标准

能不看文档回答："`|` 到底做了什么？`RunnableParallel` 什么时候用？`ToolMessage` 和 `AIMessage` 有什么区别？"

---

## 四、阶段 2：工具与 Agent 基础（约 1 周）

### 要掌握的知识

**1. `@tool` 进阶**
- `args_schema`（用 Pydantic 定义参数结构，比类型注解更可控）
- 工具内部抛异常 vs 返回错误字符串（哪种对模型更友好）
- 工具的 docstring 为什么决定模型选不选它

**2. 工具绑定的机制**
- `bind_tools([...])` 之后模型返回的 `tool_calls` 结构
- `tool_choice`（强制/禁止调用工具）
- **并行工具调用**（模型一次规划多个动作）

**3. Agent 的两种写法**
- `create_react_agent`（封装版，快速原型）
- 手写循环（LangGraph，阶段 3）
- `ToolNode`（LangGraph 提供的工具执行节点）

**4. Agent 的错误处理**
- `handle_parsing_errors`（工具调用失败自动重试）
- `max_iterations`（防死循环）
- 工具执行超时

### 产出

- [ ] 一个**多功能助手**：能查资料（网络搜索/URL 读取）+ 计算 + 读写本地文件
- [ ] 至少一个工具用 `args_schema` 定义
- [ ] 故意让一个工具抛错，验证 Agent 能优雅恢复

---

## 五、阶段 3：LangGraph 深入（约 2.5 周）★最核心

### 要掌握的知识

**1. State 设计（最重要）**
- `TypedDict` 定义 State
- `Annotated[list, add_messages]` —— reducer 的概念（**为什么消息要累加，而普通字段是覆盖**）
- 自定义 reducer（比如计数器、去重）

**2. 图的构造**
- `StateGraph` / `add_node` / `add_edge` / `add_conditional_edges` / `compile`
- `START` / `END`
- 节点返回值如何合并进 State

**3. 循环与终止**
- 条件边构成 Agent 循环
- **递归限制**（`recursion_limit`）与死循环排查
- 多节点串行、并行节点

**4. 持久化与记忆**
- `checkpointer`（`MemorySaver` / `SqliteSaver`）
- `thread_id`：如何让同一会话记住历史
- `get_state` / `update_state`（查看、修改状态）
- 时间旅行（回放某个历史点）

**5. 人工介入（Human-in-the-loop）**
- `interrupt()`：在关键步骤暂停等确认
- 恢复执行（`Command(resume=...)`）
- 适用场景：花钱操作、删数据、发消息前的确认

**6. 高级控制流**
- **子图（Subgraph）**：把复杂流程拆成模块
- **`Send` API**：动态并行（map-reduce 模式）
- 流式输出（`stream` / `stream_mode="updates"`）

### 产出

- [ ] 把 `05_langgraph_agent.py` 跑通并**改成 3 轮以上循环**（多工具串行）
- [ ] 加 `checkpointer`，实现**跨轮记忆**（第二次对话记得第一次说的名字）
- [ ] 加 `interrupt()`，在"调用某个危险工具"前**暂停等确认**
- [ ] 做一个**带分支的工作流**：根据问题类型走不同节点分支

### 检验标准

能在白板上画出"Agent 循环图"，并说清：State 里有什么、谁改它、什么条件下走哪条边。

---

## 六、阶段 4：RAG（约 2.5 周）

### 要掌握的知识

**1. 文档加载**
- `TextLoader` / `PyPDFLoader` / `Docx2txtLoader` / `Unstructured`
- 注意编码（`utf-8`）、大文件流式读取

**2. 切分（Chunking）**
- `RecursiveCharacterTextSplitter`（`chunk_size` / `chunk_overlap` 怎么选）
- 中文切分的特殊考虑（按句号/换行切）
- 语义切分（进阶）

**3. Embedding（关键限制）**
- ⚠️ **DeepSeek 没有 embedding 接口**，必须另找方案：
  - 本地 `sentence-transformers`（`BAAI/bge-small-zh-v1.5`）**推荐**
  - Ollama 本地 embedding 模型
  - 其他厂商 API
- 向量维度的概念、相似度计算（cosine）

**4. 向量库**
- `Chroma`（本地持久化，最省事）/ `FAISS`
- 建库、增量添加、持久化目录

**5. 检索策略**
- 相似度检索（`similarity_search`）
- **MMR**（避免检索结果重复）
- 多查询（MultiQuery）、混合检索（关键词+向量）
- 重排（Rerank，进阶）

**6. RAG 链**
- 基础版：检索 → 拼进提示词 → 生成
- **引用溯源**：让回答带上"出自第几段"
- 处理"检索不到"的情况（不要让模型硬编）

**7. RAG 评估**
- 准备测试集（问题 + 期望答案）
- 指标：召回率、答案准确性
- RAGAS（进阶）

### 产出

- [ ] **`course-rag`**：把 `notes/topics/` 里的 Python 笔记做成知识库
- [ ] 能回答"线程和进程怎么选"这类问题，并**给出出处**
- [ ] 至少对比两套切分参数，看效果差异

---

## 七、阶段 5：工程化与部署（约 2 周）

### 要掌握的知识

**1. 配置管理**
- `pydantic-settings` 读取 `.env`（类型校验 + 默认值）
- 环境变量分层（开发/生产）

**2. 可观测性**
- `LangSmith`（官方 trace，免费额度够用）：看每次调用的输入输出、耗时、token
- 或 `Langfuse`（开源替代）
- 关键：**能定位"是哪一步变慢了/错了"**

**3. 健壮性**
- 重试（`tenacity` / 自己写）
- 超时控制
- 降级策略（模型挂了怎么办）
- 成本控制（token 上限、缓存）

**4. 服务化**
- FastAPI **同步**接口（`def` 而不是 `async def`，够用且简单）
- 请求/响应模型（Pydantic）
- 流式响应（SSE，进阶）

**5. 部署**
- Docker 容器化
- 环境变量注入（密钥不进镜像）
- GitHub Actions 自动测试

**6. 测试**
- `pytest` 单测（**mock 掉 LLM 调用**，不要每次都真调）
- 集成测试（少量真实调用）

### 产出

- [ ] `agent-service`：把阶段 4 的 RAG 封装成 FastAPI 服务
- [ ] 有 Dockerfile，一条命令起服务
- [ ] 有 3~5 个 pytest 测试（含 mock）
- [ ] 接上 LangSmith，能看到完整 trace

---

## 八、阶段 6：高级模式（约 2 周）

### 要掌握的知识

**1. 多智能体**
- Supervisor 模式（一个主管分派任务给子 agent）
- 层级团队（team of teams）
- 何时该用多 agent（**大多数时候不该**——先单 agent 做不好再拆）

**2. 反思与自我改进**
- Reflection（自己检查答案再重写）
- Critic agent（评审 agent）
- 适用：写作、代码生成

**3. 规划模式**
- Plan-and-Execute（先列计划再执行）
- ReWOO（减少 token）

**4. 记忆体系**
- 短期（当前会话）
- 长期（跨会话，向量库存记忆）
- 语义记忆 / 情景记忆

**5. 安全与护栏**
- 输入过滤（prompt injection 防护）
- 输出校验
- 权限控制（哪些工具允许自动执行）

### 产出

- [ ] 一个**双 agent 协作**的小系统（比如"写手 + 审稿人"）
- [ ] 一个带**长期记忆**的助手（跨会话记住用户偏好）

---

## 九、阶段 7：项目集整合（约 2.5 周）

### 作品集（4 个，从易到难）

| # | 项目 | 技术点 | 面试价值 |
|---|---|---|---|
| 1 | **`course-rag`** | RAG + 向量库 + 引用溯源 | 证明你会 RAG |
| 2 | **`ai-study-agent`** | LangGraph 多轮 + 工具 + 记忆 | 证明你会 Agent |
| 3 | **`neurocards-ai`** | Agent 自动生成记忆卡片（**呼应 P1 的 neurocards**） | 证明你有系统思维 |
| 4 | **`agent-service`** | FastAPI + Docker + 测试 + trace | 证明你能交付 |

### 简历包装（STAR）

每个项目写清楚：
- **情境**：解决什么问题
- **任务**：你负责什么
- **行动**：用了什么技术、为什么这么选
- **结果**：**量化**（准确率、响应时间、覆盖多少文档）

### 收尾

- [ ] 每个项目都有：README + 演示截图/录屏 + 测试
- [ ] GitHub 仓库整理（pin 到主页）
- [ ] 挑 2 个能**深入讲 15 分钟**的

---

## 十、每个阶段都要做的三件事

1. **动手改**：跑通后至少改一处（换模型、加工具、改条件），看行为变化
2. **写笔记**：新增/更新 `notes/topics/`，跑 `build_index.py`
3. **提交**：`git add . && git commit -m "阶段X: xxx" && git push`

---

## 十一、常见坑速查（会反复遇到）

| 坑 | 现象 | 解法 |
|---|---|---|
| DeepSeek 不支持 `json_schema` | `This response_format type is unavailable now` | `with_structured_output(..., method="function_calling")` |
| DeepSeek 没有 embedding | RAG 无法向量化 | 本地 `bge-small-zh` / Ollama |
| `ToolMessage` 缺 `tool_call_id` | 报错或工具结果丢失 | 用 `ToolNode` 自动处理 |
| 忘记 `checkpointer` | 多轮对话记不住 | 建图时传 `checkpointer` + 调用时传 `thread_id` |
| 条件边不返回 `END` | 死循环/递归超限 | 明确返回 `END`，设 `recursion_limit` |
| 状态被覆盖而非累加 | 历史消息消失 | 字段加 `Annotated[list, add_messages]` |
| `bind_tools` 后模型乱调工具 | 工具描述不清 | 把 docstring 写具体，用 `args_schema` |

---

## 十二、学习资源

| 内容 | 资源 |
|---|---|
| LangChain 官方 | <https://python.langchain.com> |
| LangGraph 官方 | <https://langchain-ai.github.io/langgraph/> |
| 官方教程（最该看） | LangGraph 的 "Learn" 部分，有交互式 notebook |
| DeepSeek 文档 | <https://platform.deepseek.com/api-docs> |
| 本地 embedding | `BAAI/bge-small-zh-v1.5`（HuggingFace） |
| 可观测 | <https://smith.langchain.com> |

---

## 十三、一句话总结

> **阶段 0~2 是"会用"，阶段 3 是"会搭"，阶段 4 是"会接数据"，阶段 5 是"会交付"，阶段 6 是"会做复杂系统"，阶段 7 是"会包装"。**
> 走完这 7 个阶段，你就不是"学过 LangChain 的人"，而是"能用它做产品的人"。
