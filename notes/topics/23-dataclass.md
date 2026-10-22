---
title: dataclass
category: 进阶
keywords: [dataclass, 类, 字段声明, frozen, field, init=False, __post_init__, 校验, 不可变]
dates: [2026-10-22]
---

# dataclass

> 一句话：`@dataclass` 自动帮你生成 `__init__` / `__repr__` / `__eq__`，**写一个只有字段的类时几乎是必用**。

## 1. 最基础的用法

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(1, 2)
print(p)            # Point(x=1, y=2)   ← __repr__ 自动生成
print(p == Point(1, 2))   # True         ← __eq__ 自动生成
```

不用手写 `__init__`，字段声明完就有构造函数。

## 2. ⚠️ 类型注解是必须的（最关键的一点）

> 在 `dataclass` 里，**`name: str` 是「字段声明」，`name = '默认值'` 是「类属性」**，两者作用截然不同。

```python
@dataclass
class Demo:
    a: int          # 这是字段，会进 __init__
    b: int = 10     # 这是有默认值的字段，也会进 __init__
    c = 20          # 没有类型注解 → 被当成普通类属性，不会进 __init__


d = Demo(1)          # 只能传 a、b
print(d)             # Demo(a=1, b=10)
print(d.c)           # 20
```

| 写法 | 是什么 | 进 `__init__` 吗 |
| --- | --- | --- |
| `a: int` | 字段声明 | ✅ |
| `b: int = 10` | 有默认值的字段 | ✅ |
| `c = 20` | 普通类属性 | ❌ |

> 这就是为什么 [20-类型注解](20-类型注解.md) 要先学——`dataclass` **靠类型注解识别字段**。

## 3. 字段默认值的坑

```python
@dataclass
class Bad:
    tags: list = []      # ❌ ValueError: mutable default
```

和「函数可变默认参数」是同一个坑。解决办法：

```python
from dataclasses import dataclass, field

@dataclass
class Good:
    tags: list = field(default_factory=list)      # ✅ 每次新建一个列表
    scores: dict = field(default_factory=dict)
```

## 4. `frozen=True`：创建后不可变

适合「坐标点、枚举值、配置项」这种概念上就该只读的东西。

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
p.x = 100          # ❌ FrozenInstanceError: cannot assign to field 'x'
```

> 这个保护是**运行时**的——就算静态检查工具没拦住，运行时也会炸。
> 附带好处：`frozen=True` 的对象**可哈希**（能放进 `set` / 当 `dict` 的 key），
> 解决了 [13-特殊方法与哈希](13-特殊方法与哈希.md) 里"重写 `__eq__` 就不可哈希"的麻烦。

| 写法 | 能不能改 | 可哈希 |
| --- | --- | --- |
| `@dataclass` | ✅ 能改 | ❌（默认 `eq=True` 时不可哈希） |
| `@dataclass(frozen=True)` | ❌ 不能改 | ✅ |

## 5. `field(init=False)`：派生字段

从其他字段算出来的值，不该让用户在构造时传。

```python
@dataclass
class Order:
    price: float
    count: int
    total: float = field(init=False)      # 不出现在 __init__ 参数里

    def __post_init__(self):
        self.total = self.price * self.count


o = Order(9.9, 3)      # 只传 price 和 count
print(o.total)         # 29.7
```

> `init=False` 让 `total` **不出现在 `__init__` 的参数里**——用户构造时不需要也不该传它。

## 6. `__post_init__`：构造后自动调用的钩子

> `__post_init__` 是 `dataclass` **自动调用**的，名字必须就是这个，**连下划线数量都不能错**（前后各两个）。

两种典型用途：

### 用途 A：派生计算（推荐）

```python
def __post_init__(self):
    self.total = self.price * self.count
```

### 用途 B：字段校验（可用，但是权宜之计）

```python
@dataclass
class Employee:
    name: str
    salary: int

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError(f'工资不能是负数，收到: {self.salary}')
        if not self.name:
            raise ValueError('姓名不能为空')


Employee('两点水', -100)     # ❌ ValueError: 工资不能是负数，收到: -100
Employee('两点水', 12000)    # ✅ Employee(name='两点水', salary=12000)
```

> ⚠️ **但 `__post_init__` 里写校验只是「权宜之计」**。它的活儿性质偏向「派生计算」，
> 校验逻辑写多了会显得别扭。**生产里如果数据来自外部（HTTP 请求、JSON 配置），更推荐用 Pydantic 专门做校验。**

## 7. dataclass / 普通类 / Pydantic 怎么选

| 场景 | 选什么 |
| --- | --- |
| 只是装数据的容器（内部使用） | **dataclass** |
| 需要只读、可哈希 | `dataclass(frozen=True)` |
| 有复杂校验、数据来自外部（API/JSON） | **Pydantic**（`BaseModel`） |
| 有大量业务方法、状态会变 | 普通类 |

> 顺带：**Agent 开发里的工具参数、结构化输出**用的就是 Pydantic，和 dataclass 思路一脉相承。

## ⚠️ 易错点速记

1. **没有类型注解的字段不会进 `__init__`**（会变成类属性）——最容易踩
2. 可变默认值（`list`/`dict`/`set`）必须用 `field(default_factory=...)`
3. `frozen=True` 只是**运行时**保护，改不动是真改不动，但也别指望它是"编译期检查"
4. `field(init=False)` 的字段要在 `__post_init__` 里赋值，否则读它是 AttributeError
5. `__post_init__` 前后各两个下划线，写错就静默不执行
6. 校验别全塞 `__post_init__`，外部数据用 Pydantic
7. 默认 `@dataclass` 不可哈希（因为自动生成了 `__eq__`），需要时加 `frozen=True`

## 🔗 关联

- 类型注解（dataclass 的基础）→ [20-类型注解](20-类型注解.md)
- 类属性与实例属性 → [15-类属性与实例属性](15-类属性与实例属性.md)
- 特殊方法与哈希 → [13-特殊方法与哈希](13-特殊方法与哈希.md)
- 可变默认参数（同一个坑）→ [11-函数进阶](11-函数进阶.md)
- 原始截图 → [source/2026-10-22/A.md](../source/2026-10-22/A.md)（图 image67~image70）
