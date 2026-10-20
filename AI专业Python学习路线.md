# AI 专业 · Python 从零到精通 · 学习路线（GitHub 作品导向版）

> 适用对象：人工智能专业在读，有一定数学/算法基础，Python 零基础或只会写脚本。
> 目标：把 Python 学到**能看懂 CPython 机制、能写工程级代码、能把模型做成产品**的程度，并积累一套别人抄不走的 GitHub 作品。
> 节奏建议：每天 3–4 小时有效学习，总周期约 **12 个月**（比原计划更聚焦"精通 + 作品"，而非赶进度）。

---

## 一、三条贯穿始终的原则（先读，再往下）

1. **项目驱动，不是教程驱动**。每个阶段末尾必须交付一个能发 GitHub 的项目；视频/书只是"查字典"，项目才是"学语言"。
2. **双轨并行**：主线学 Python/ML 工程，副线每天刷 1–2 题算法 + 按需补数学。两条线都不断，才不会"会用但写不深"。
3. **证据优先**。每个项目都要有 README、测试、训练日志、量化结论。面试官只信"你解决过什么、用什么方法、结果如何"，不信"我熟悉 xx"。

**学习思路（方法论）**，贯穿所有阶段：

- 每学一个知识点，**立刻手写代码验证**，不要看完视频就以为会了。
- 报错先自己读 30 分钟再搜，养成调试耐心。
- 用 **git 小步提交**（每完成一个功能 commit 一次），这既是工程习惯，也是你的"成长轨迹"。
- 官方文档 > 二手视频 > 公众号文章。到了第 3 阶段以后，一定要逼自己直接读英文文档和论文。
- 输出倒逼输入：每个项目写 README 时用"费曼法"——把项目讲给一个不懂的人听，讲不清的地方就是没学会。

---

## 二、总时间表（我自己重新规划的节奏）

| 阶段 | 主题 | 周期 | 交付物（GitHub 项目） |
|---|---|---|---|
| P0 | 环境 + Git + 编程思维 | 1 周 | `py-bootcamp` 学习日志仓库 |
| P1 | Python 核心语法 + 高级特性 | 约 5 周 | `neurocards` 终端间隔重复背题系统 |
| P2 | 数据科学（NumPy/Pandas/可视化） | 约 5 周 | `ai-job-market-report` AI 就业市场数据分析报告 |
| P3 | 工程基本功 + 机器学习 | 约 6 周 | `ml-eval-kit`（发布 PyPI）+ 1 个端到端 ML 项目 |
| P4 | 深度学习（PyTorch） | 约 7 周 | CNN（手写中文识别）+ NLP（情感分类）两个项目 |
| P5 | AI 工程化（FastAPI/Docker/CI） | 约 4 周 | `model-serving` 模型推理服务 |
| P6 | 大模型应用（RAG + Agent） | 约 8 周 | `course-rag` + `ai-study-agent`（部署上线） |
| P7 | 求职冲刺 | 与 P6 并行 | 作品集网站 + STAR 简历 + 开源贡献 |

**副线（每天并行，不占主线大块时间）**：

- 算法：LeetCode，从 Easy 到 Medium，重点数组/哈希/字符串/二叉树/图。
- 数学：线性代数、概率统计按需补（AI 专业课程进度没跟上时补）。
- 英语：坚持读英文文档和论文，不要只靠中文翻译。

---

## 三、P0 · 环境与编程思维（第 1 周）

**学什么**

- 装 **Miniconda**（比 Anaconda 轻，同样能一键装 NumPy/Pandas/Jupyter；想要省事用 Anaconda 也行）。
- IDE 用 **VS Code**（AI 生态更好，配 Python/Jupyter 插件）；PyCharm Community 也可。
- 装 **Git** 并注册 GitHub，配好 SSH key、`.gitignore`。
- 理解"程序 = 按顺序执行的指令"，跑通第一个脚本和第一个 Jupyter 单元格。

**动手做**

- 在 Jupyter 里完成 10 个迷你练习：变量交换、简易计算器、温度/单位换算、猜数字、九九乘法表、斐波那契、字符串反转、列表去重、字典统计词频、读写一个 txt 文件。
- 每天 30 分钟"读报错 + 自己解决"。

**产出：`py-bootcamp`**

- 一个仓库，内含：环境搭建说明（别人照着能复现）、10 个练习脚本（带注释）、一个 `daily-log.md` 学习日志。
- **开创点**：从第 1 天就建立"公开记录学习过程"的习惯——这份日志本身就是你求职时"持续学习"的证据。

**完成标准（清单）**

- [ ] 能 `conda create` 建环境、`pip` 装包、知道为什么用虚拟环境
- [ ] 能 `git clone / add / commit / push`，提交历史清晰
- [ ] Jupyter 跑通 10 个练习并推到 GitHub

---

## 四、P1 · Python 核心语法 + 高级特性（约 5 周）

**学什么（顺序）**

1. 基础：变量、类型（int/float/str/bool）、条件、循环、`range`、输入输出。
2. 容器：list/tuple/dict/set，**列表推导式**（一定要练到顺手）。
3. 函数：定义、参数（默认/关键字/`*args`/`**kwargs`）、作用域、`return`。
4. 字符串与文件：格式化 f-string、`with open`、CSV/JSON 读写、`pathlib`。
5. 异常处理：`try/except/finally`、自定义异常。
6. 面向对象：类、`__init__`、实例/类属性、继承、`@property`、`dataclass`。
7. **进阶（通往"精通"的关键）**：装饰器、生成器 `yield`、上下文管理器 `with`、`itertools`/`collections`/`functools`、类型注解 `typing`、模块与包。

**免费资源（按推荐顺序）**

- [CS50P（哈佛 Python）](https://cs50.harvard.edu/python/) —— 免费，思维训练一流，B 站有中字。
- [廖雪峰 Python 教程](https://liaoxuefeng.com/books/python/introduction/) —— 免费中文，适合查漏。
- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) —— 权威，进阶必读。
- [learn-py.org](https://learn-py.org) —— 浏览器内交互练习。
- [Real Python](https://realpython.com) —— 免费英文文章，进阶专题（装饰器/生成器/元类）讲得极好。
- 算法副线：[代码随想录](https://programmercarl.com)（免费中文，算法四件套）+ [LeetCode](https://leetcode.cn)。

**产出：`neurocards` —— 终端间隔重复背题系统**

- 定位：一个命令行里的"记忆卡片"工具，用 **SM-2 算法**（Anki 同款）安排复习时间。
- 技术栈：`argparse`/`click` + `json`/`sqlite3` + `datetime` + 面向对象（卡片类、牌组类、复习调度类）。
- 功能：加卡片、按记忆曲线抽卡复习、按"生疏程度"评分、进度存 SQLite、数据导出。
- **开创点**：不是又一个人人都在做的 todo/记账复刻；SM-2 是真实算法，能锻炼"把算法翻译成代码"的能力；而且它直接服务你**自己背书复习**，以后 P6 会用它做"AI 自动出题"。
- 进阶加分项：写 `pytest` 单元测试（从这一步开始养成测试习惯）。

**完成标准（清单）**

- [ ] 推导式、装饰器、生成器、上下文管理器每个都能默写一个例子
- [ ] LeetCode Easy 累计完成 40+ 题
- [ ] `neurocards` 有 README、可安装运行、有测试、推上 GitHub

---

## 五、P2 · 数据科学核心工具链（约 5 周）

**学什么**

- NumPy：`ndarray`、切片/花式索引、**广播机制**、向量化、矩阵运算。
- Pandas：`DataFrame` 的筛选、`groupby`、`merge`、`pivot_table`、`apply`、时间序列。
- 可视化：Matplotlib 基础 + Seaborn 统计图。
- 数据思维：清洗（缺失值/重复/异常）、描述性统计、如何从数据里提出一个"能回答的问题"。

**免费资源**

- [Kaggle Learn](https://www.kaggle.com/learn) —— 免费微课程，Pandas/数据可视化各 3–4 小时。
- [Datawhale 开源学习](https://github.com/datawhalechina) —— 免费中文，组队学习路线非常系统。
- [pandas 官方文档](https://pandas.pydata.org/docs/) + [10 分钟入门](https://pandas.pydata.org/docs/user_guide/10min.html)。
- [天池](https://tianchi.aliyun.com) —— 国内数据集与入门赛。
- 重点死磕 `groupby`、`merge`、`pivot_table` —— 这是面试最高频。

**产出：`ai-job-market-report` —— AI 就业市场数据分析报告**

- 定位：用**真实招聘数据**（公开的 AI 岗位 JD 数据集，Kaggle/天池或自己爬招聘站），回答一个与你切身相关的问题：**"AI 岗位到底在招什么样的人？"**（高频技能、学历要求、薪资分布、不同城市/岗位差异）。
- 流程：CSV 读取 → 清洗 → 分组统计 → 可视化 → 输出结论，写成一篇有叙事的数据报告。
- **开创点**：不做烂大街的 Titanic/房价分析；选题直击你自己的求职目标，结论对你选择方向（算法/工程/数据）有真实指导意义——面试时这是"有故事、有量化结论"的项目。
- 发布方式：Jupyter Notebook + 用 [Quarto](https://quarto.org) 或 GitHub Pages 渲染成网页报告。

**完成标准（清单）**

- [ ] 能解释清楚 NumPy 广播在什么情况下会报错
- [ ] 用 `groupby/merge/pivot_table` 各解决过一个真实统计问题
- [ ] 报告有"数据来源 → 方法 → 结论 → 局限"，并发布成网页

---

## 六、P3 · 工程基本功 + 机器学习（约 6 周）

**学什么**

- **工程基本功（先花 2 周，这是"精通"的分水岭）**：虚拟环境与依赖管理（`uv` 或 `pip` + `pyproject.toml`）、**打包发布到 PyPI**、`pytest` 测试、`ruff` 静态检查、日志 `logging`、`cProfile` 性能剖析、把代码组织成规范的包结构。
- **机器学习**：监督学习（线性/逻辑回归、决策树、随机森林、SVM）、无监督（K-Means、PCA）、模型评估（交叉验证、混淆矩阵、ROC-AUC）、特征工程（标准化、独热编码、特征选择）。
- 完整走"数据准备 → 训练 → 调参 → 评估"流程，自己换数据集、改参数、观察变化。

**免费资源**

- [吴恩达 Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)（旁听免费）。
- [李宏毅机器学习](https://speech.ee.ntu.edu.tw/~hylee/ml/)（免费，B 站有）。
- [scikit-learn 官方文档](https://scikit-learn.org/stable/) —— 每个 API 都有例子。
- [Hands-On ML（第 3 版）配套 Notebook](https://github.com/ageron/handson-ml3) —— 免费。
- 数学副线：3Blue1Brown [线性代数的本质](https://www.3blue1brown.com/topics/linear-algebra)（B 站有中文）+ 概率统计。

**产出 A：`ml-eval-kit` —— 一个小型"模型对比/评估"工具库（发布到 PyPI）**

- 定位：把"跑 N 个模型 × M 个指标、输出对比表/图"这件事做成一个 `pip install` 就能用的库。
- **开创点**：绝大多数人只写 Notebook，而你交付的是一个**别人能 `pip install` 的包**（带类型注解、测试、CI、文档）。这一项就能让你的简历和"只会跑教程的人"拉开差距。
- 顺带完成：发布流程、语义化版本、GitHub Actions 自动跑测试。

**产出 B：1 个端到端 ML 项目（回归或分类二选一，用真实数据）**

- 建议选题（避开房价/Iris）：能源负荷预测（回归）、用户流失预测（分类）、或延续 P2 的招聘数据做"薪资区间预测"。
- 交付：特征工程 + 多模型对比 + 评估报告，README 写清"目标→方法→结果→局限"。

**完成标准（清单）**

- [ ] `ml-eval-kit` 成功发布到 PyPI，`pip install` 后能跑通
- [ ] 每个模型都能说清"为什么选它、超参怎么调、指标怎么看"
- [ ] 能向别人讲清 ROC-AUC、交叉验证、过拟合/欠拟合

---

## 七、P4 · 深度学习（PyTorch）（约 7 周）

**学什么**

- PyTorch：Tensor 操作、自动求导 `autograd`、`nn.Module`、`Dataset/DataLoader`、GPU 训练。
- 经典网络：MLP、CNN、RNN/LSTM。
- 训练技巧：学习率调度、正则化（Dropout/权重衰减）、早停、混合精度。
- **实验纪律**：每次改动只改一个变量，记录训练日志，做**消融实验**。

**免费资源（务必用中文资源打底，英文进阶）**

- [《动手学深度学习》d2l.ai](https://zh.d2l.ai) —— **免费中文，强烈推荐**，李沐，代码可直接跑。
- [PyTorch 官方 60 分钟入门](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)。
- [CS231n（斯坦福 CV）](https://cs231n.github.io) —— 免费。
- [fast.ai](https://course.fast.ai) —— 免费，工程视角。

**产出 A：CNN 图像分类 —— 手写中文识别（差异化选题）**

- 定位：在中文手写字符数据集上训练 CNN（而非人人都在做的 CIFAR-10/手写数字）。
- **开创点**：选题更贴合中文环境、更有区分度；把训练过程写成一篇 **mini-paper**——含数据说明、架构选择理由、消融实验（加不加 BN、换激活函数、调学习率各自的影响）、错误分析（哪些字最容易错、为什么）。
- 交付：代码 + 训练日志（tensorboard/wandb）+ 结果分析。

**产出 B：NLP 文本分类（情感分类）**

- 定位：IMDB 或中文影评情感分类，体验文本数据处理与图像的不同（分词、词表、padding、Embedding）。
- 交付：至少 LSTM 和（如果时间允许）一个预训练模型微调两条路线，对比结果并写清楚差异。

**完成标准（清单）**

- [ ] 能解释反向传播、`DataLoader` 的 batch 流程、为什么 GPU 训练更快
- [ ] 两个项目都有训练日志和消融实验，而非"只贴最终准确率"
- [ ] 能说清"遇到 loss 不降/过拟合时你怎么排查"

---

## 八、P5 · AI 工程化（约 4 周）

**学什么**

- 异步编程：`async/await`（推理服务是 I/O 密集，异步是基础）。
- FastAPI：构建模型推理 API，自动生成 OpenAPI 文档。
- Docker：把服务容器化，做到"另一台机器一键启动"。
- Git 协作：feature branch → PR → Code Review；GitHub Actions CI/CD。

**免费资源**

- [FastAPI 官方文档](https://fastapi.tiangolo.com) —— 教程质量极高。
- [Docker Get Started](https://docs.docker.com/get-started/)。
- [GitHub Skills](https://skills.github.com) —— 免费交互式 Git 练习。
- [Pro Git（中文）](https://git-scm.com/book/zh/v2)。

**产出：`model-serving` —— 模型推理服务**

- 定位：把 P4 训练好的一个模型封装成 FastAPI 接口，写请求测试脚本，用 Docker 容器化。
- 交付：`Dockerfile` + API 文档 + README + 一个简单的压测/延迟测量结果（异步 vs 同步对比）。
- **开创点**：这是你简历上"把模型变成产品"的直接证据，是"研究+工程复合型"最有力的注脚。

**完成标准（清单）**

- [ ] 接口能接收图片/文本、返回预测，文档自动生成
- [ ] `docker build && docker run` 一条命令起服务
- [ ] 能说清同步/异步、多进程/多线程在推理服务里怎么选

---

## 九、P6 · 大模型应用开发（约 8 周，核心赛道）

**学什么**

- Prompt Engineering：系统提示词、few-shot、链式思考。
- RAG：Embedding、向量数据库（如 Chroma/Faiss）、检索策略、分块。
- Agent：LangChain/LangGraph、工具调用（function calling）、记忆管理。
- 微调基础：LoRA/QLoRA、Hugging Face 生态（了解即可，先不必深入）。

**免费资源**

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) —— 免费。
- [DeepLearning.AI 短课程](https://www.deeplearning.ai/short-courses/) —— 大量免费，RAG/Agent 专题。
- [LangChain 文档](https://python.langchain.com) / [LangGraph](https://langchain-ai.github.io/langgraph/)。
- [李宏毅 LLM 课程](https://www.youtube.com/@HungyiLeeNTU)（B 站有）+ [Datawhale 大模型教程](https://github.com/datawhalechina)。
- 本地模型用 [Ollama](https://ollama.com) 免费跑开源模型。

**产出 A：`course-rag` —— 专业课程知识库问答**

- 定位：把你**本专业的课程资料**（教材/课件/笔记）做成知识库，实现"基于文档的问答"。
- **开创点**：知识库选你自己的专业，能真正用起来复习考试；顺带解决"教材内容被分块切碎后答案不准"这类真实工程问题（分块策略、重排、引用溯源）。
- 加分：做**本地优先**版本（Ollama + 本地向量库），突出隐私与零成本。

**产出 B：`ai-study-agent` —— 学习陪伴 Agent（呼应 P1）**

- 定位：一个能调用工具的 Agent——搜索、计算、**自动调用 `neurocards` 生成复习卡片**，完成"读一段材料 → 出题 → 安排复习"的多步骤任务。
- **开创点**：把你 P1 的背题系统用 Agent 串起来，形成一个**首尾呼应的作品弧线**——面试官会看到你不是零散堆项目，而是有系统思维。部署上线，给一个公网可访问的 Demo。

**完成标准（清单）**

- [ ] RAG 能回答课程问题并给出"出处引用"
- [ ] Agent 能完成一次多步骤任务（调用 ≥2 个工具）
- [ ] Demo 公网可访问，README 有演示截图/录屏

---

## 十、P7 · 求职冲刺（与 P6 后半段并行，约 6–8 周）

**简历与作品包装**

- 每个项目用 **STAR 法则**重写：情境→任务→行动→结果（量化：准确率提升多少、响应降到多少、覆盖多少数据）。
- 做一个人作品集网站（GitHub Pages 即可），把 7 个项目按"能力图谱"陈列。
- 挑 2–3 个能**深入讲 15 分钟**的项目，准备好被追问的细节。

**面试准备**

- 算法岗补数据结构与数学；工程岗补系统设计与代码能力。**别把精力耗在追新名词上。**
- LeetCode 以 Medium 为主，覆盖数组/字符串/哈希/二叉树/图；用代码随想录过一遍题型。
- 准备"项目深挖"：每个项目能讲清"为什么这么设计、踩过什么坑、怎么解决的"。

**投递策略**

- 先分清方向：底层算法研究岗 / 工程部署应用岗 / 数据评测支撑岗。
- 对**应届生**而言，AI 应用开发岗与 AI 工程岗的入门门槛明显低于纯算法研究岗——你的"研究+工程"复合定位正好卡在这个最有需求的区间。

**开源贡献（画龙点睛）**

- 挑一个你在用的库（pandas / sklearn / langchain / 某个小工具），从"修文档/小 bug"开始提交 1–2 个 PR。这是"开源贡献者"身份，含金量高于再堆一个教程项目。

---

## 十一、整条路线的"作品弧线"（一句话回顾）

> `py-bootcamp`（记录）→ `neurocards`（写算法）→ `ai-job-market-report`（读数据）→ `ml-eval-kit`（做工具）→ 深度学习 mini-paper（做实验）→ `model-serving`（做产品）→ `course-rag` + `ai-study-agent`（做系统）。

这条线串起来就是一个完整的故事：**"我从零开始，最终把模型变成产品、用 Agent 把工具串成系统。"** 这比十个孤立教程项目有说服力得多。

---

## 附：学习清单总表（打印贴墙版）

- [ ] P0：环境跑通 + 10 个练习 + 学习日志仓库
- [ ] P1：核心语法 + 高级特性 + LeetCode Easy 40+ + `neurocards`
- [ ] P2：NumPy/Pandas/可视化 + `ai-job-market-report`
- [ ] P3：打包发布 + ML + `ml-eval-kit`（PyPI）+ 端到端项目
- [ ] P4：PyTorch + CNN/NLP 两个 mini-paper 项目
- [ ] P5：FastAPI/Docker/CI + `model-serving`
- [ ] P6：RAG + Agent + `course-rag`/`ai-study-agent`（上线）
- [ ] P7：STAR 简历 + 作品集 + 开源贡献 + LeetCode Medium

---

## 附录：三个「硬伤」的补丁方案

> 背景：目前在用的 [learn-py.org](https://learn-py.org)（29 章 / 约 104 道题 / 约 14 小时内容）是一个优秀的**语法加速器**，但它有三个结构性缺口。它不是"错了"，而是**分工不同**——下面的方案负责补齐另一半。

### 硬伤 1 — 没有 NumPy / Pandas / Matplotlib

| 项 | 内容 |
|---|---|
| 补法 | 网站刷完 00~22 章后进入 P2 阶段，用另一套资源补数据栈 |
| 资源 | [Kaggle Learn](https://www.kaggle.com/learn) 三门微课：Python → Pandas → Data Visualization（各 3~4 小时，免费，自带练习环境）；中文补充 [Datawhale](https://github.com/datawhalechina) |
| 落地项目 | `ai-job-market-report`（真实招聘数据分析报告） |
| 时间点 | 网站刷完后（P2，约 5 周） |
| 验收标准 | 能**独立**完成：读 CSV → 清洗 → `groupby` → 画图 → 写出结论 |

**最小掌握清单**（别被吓到，核心就 6 个操作）：`read_csv`、`head/describe`、条件筛选、`groupby`、`merge`、`pivot_table` + 3 种图（折线/柱状/散点）。

### 硬伤 2 — 没有真项目

| 层级 | 项目 | 说明 |
|---|---|---|
| 小（P1） | `neurocards` | 桌面已给骨架，从 M1 开始写 |
| 中（P2） | `ai-job-market-report` | 数据分析报告 |
| 大（P3） | `ml-eval-kit` | 发布到 PyPI，别人能 `pip install` |
| 大（P5/P6） | `model-serving`、`course-rag`、`ai-study-agent` | 部署上线 |

原则：**完整性 > 复杂度**。3 个完整的小项目 > 1 个烂尾的大项目。

### 硬伤 3 — 工程章节是「只读」的

| 网站章节 | 强制落地任务 | 对应里程碑 |
|---|---|---|
| `pytest` | 删掉 `neurocards/tests/test_sm2.py` 的 7 个 skip，跑绿 | M3 |
| `pyproject + uv` | 把 `neurocards` 改造成 `pyproject.toml` + `src/` 结构 | M6 |
| `ruff` | 在自己代码上跑 `ruff check .`，修完全部警告 | M6 |
| `logging` | 把 `neurocards` 里的 `print` 换成 `logging` | M6 |
| `PyPI` | P3 阶段**真的**把 `ml-eval-kit` 发上 PyPI | P3 |

> 工程技能不可能靠读学会，必须有一次「我真的发布了一个包」的经历。

### 补齐时间线

```text
现在      neurocards（P1）—— 硬伤2 在这里开始补；硬伤3 在 M6 补
1~2 周后  learn-py.org 00~22 章刷完（语法加速完成）
之后      Kaggle Learn + ai-job-market-report（P2）—— 硬伤1 在这里补
再后      ml-eval-kit 发 PyPI（P3）—— 硬伤3 的 PyPI 部分补完
```

### 一句话总结

**网站负责「语法手感」，neurocards 负责「把语法变成项目」，Kaggle Learn 负责「补数据栈」，PyPI 发布负责「把工程章节变成真本事」。四件事各司其职，谁也别指望谁包办。**
