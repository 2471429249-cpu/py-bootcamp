# Python 学习笔记 · 截图转写（2026-10-22 新增部分）

> 来源：`py-bootcamp/新建 DOC 文档.doc`（累积文档，本次共 70 张截图）。前 66 张已在前五次转写完成，
> 本次新增 **4 张**（image67 ~ image70），**无手写正文**。
>
> 今日截图主题：**dataclass 深入**（类型注解的作用、`frozen=True`、`field(init=False)`、`__post_init__` 校验）。

> 转写约定
> - 代码逐字保留：缩进、空行、符号、运算符、引号一律按原图照抄，不改写、不省略。
> - 表格、灰底行内代码（圆角浅灰底）、深色代码块按原样式还原为 Markdown 形式。
> - 图中被裁切的残缺行、语法高亮／下划线等排版差异，单独用「转写说明」标出，与正文内容区分。

---

## 图 image67

知识点：**dataclass 里类型注解是必须的**——`name: str` 是「字段声明」，`name = '默认值'` 是「类属性」，两者作用截然不同。

类型注解必须有

那「类型注解」是不是必须的？**是的**。这是 `dataclass` 识别字段的依据。你如果只写 `name = ''` 而不写 `name: str`，`dataclass` 就认不出来——它会把 `name` 当成一个普通的类属性，不会进 `__init__` 的参数列表。

记住一句话：在 `dataclass` 里，`name: str` 是「字段声明」，`name = '默认值'` 是「类属性」，两者作用截然不同。

```python
from dataclasses import dataclass


@dataclass
class Demo:
    a: int          # 这是字段，会进 __init__
    b: int = 10     # 这是有默认值的字段，也会进 __init__
    c = 20          # 注意：这里没有类型注解，被当成普通类属性，不会进 __init__


d = Demo(1)
print(d)
print(d.c)
```

> **转写说明**：代码块右上角有「复制」「▶ 试运行」按钮。「是的」加粗；`dataclass`、`name = ''`、`name: str` 等为行内代码样式。
> 三行注释在原图中为浅色。`c = 20` 那行的注释明确标出"没有类型注解 → 不进 `__init__`"。

---

## 图 image68

知识点：**`frozen=True` 让 dataclass 不可变**——赋值会抛 `FrozenInstanceError`。

但有时候你希望对象创建之后就不再变了——比如「坐标点」、「枚举值」、「配置项」这种概念上就该是只读的东西。这时候就该 `frozen=True` 上场：

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
print(p)

try:
    p.x = 100
except Exception as e:
    print(type(e).__name__, ':', e)
```

输出：

```text
Point(x=1, y=2)
FrozenInstanceError : cannot assign to field 'x'
```

赋值就抛 `FrozenInstanceError`。这个保护是「运行时」的——也就是说就算静态检查工具没拦住你，运行时也会炸。

> **转写说明**：`frozen=True` 与 `FrozenInstanceError` 为浅灰圆角底行内代码样式。
> 末段「运行时」加粗。输出块中两行为实际运行结果。

---

## 图 image69

知识点：**`field(init=False)` 与 `__post_init__` 的两个细节**。

这里有两个细节，重点看：

1. `total: float = field(init=False)` —— `init=False` 让 `total` 不出现在 `__init__` 的参数里。用户构造 `Order` 的时候不需要也不该传 `total`
2. `__post_init__` 是 `dataclass` 自动调用的，名字必须就是这个，**连下划线数量都不能错**

> **转写说明**：两条为有序列表，序号后为行内代码样式。第二条「连下划线数量都不能错」加粗。
> 本图是长图（969×169）的中段截取，上下文见 image70。

---

## 图 image70

知识点：**在 `__post_init__` 里做校验**——构造时检查字段是否合法。

在 post_init 里做校验

那如果想在构造时校验字段呢？也是 `__post_init__` 的活儿：

```python
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    salary: int

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError(f'工资不能是负数，收到: {self.salary}')
        if not self.name:
            raise ValueError('姓名不能为空')


try:
    bad = Employee('两点水', -100)
except ValueError as e:
    print('炸了: ', e)

ok = Employee('两点水', 12000)
print(ok)
```

输出：

```text
炸了:  工资不能是负数，收到: -100
Employee(name='两点水', salary=12000)
```

不过注意，`__post_init__` 里写校验只是「权宜之计」。它的活儿性质偏向「派生计算」，校验逻辑写多了会显得别扭。生产里如果数据来自外部（HTTP 请求、JSON 配置），更推荐用 Pydantic 这类库专门做校验。

> **转写说明**：标题为「在 post_init 里做校验」。`__post_init__` 均为行内代码样式。
> 末段「权宜之计」「派生计算」加粗。输出块首行原文是两个空格后再接文字。

---

## 本次涉及的专题

| 专题 | 对应截图 |
| --- | --- |
| [23-dataclass](../../topics/23-dataclass.md) | image67 ~ image70 |
| [20-类型注解](../../topics/20-类型注解.md)（基础回顾） | image67 |

---

## 附：今日另有 Agent 开发实践（非截图内容）

除上面 4 张截图外，今天还完成了 **Agent 应用开发环境搭建**（LangChain / LangGraph / Langflow + DeepSeek 接入）。
该部分不来自截图，见当日日记与专题：

- [24-Agent 开发环境与 DeepSeek 接入](../../topics/24-Agent开发环境与DeepSeek.md)
- [25-Langflow 基础操作](../../topics/25-Langflow基础操作.md)
