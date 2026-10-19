---
title: Enum 枚举
category: 进阶
keywords: [Enum, 枚举, IntEnum, name, value, 魔法值, 状态机, 常量]
dates: [2026-10-19]
---

# Enum 枚举

> 一句话：当「这个变量只能取固定的几个值」时，用 `Enum` 给它上**防伪标签 + 防盗锁 + 说明书**，杜绝拼写错误和魔法值。

## 1. 为什么需要枚举

```python
# ❌ 魔法值：拼错了不报错，运行时才发现
STATUS_PENDING = 0
STATUS_RUNNING = 1

status = 2          # 2 是什么？看代码的人不知道
if status == 3:     # 写错了也不报错，逻辑静默出错
    ...
```

```python
# ✅ 用 Enum：拼错立刻 AttributeError
from enum import Enum

class Status(Enum):
    PENDING = 0
    RUNNING = 1
    DONE = 2

status = Status.PENDING
if status == Status.RUNING:      # ❌ AttributeError，拼错当场暴露
    ...
```

> 用你自己的话说：普通类是个「装变量的盒子」，`Enum` 相当于给这个盒子上了
> **防伪标签、防盗锁、说明书（`name`/`value`）**，并且杜绝了任何拼写错误和恶意篡改。

## 2. 基本用法：name 与 value

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)      # RED
print(Color.RED.value)     # 1
print(Color.RED)           # Color.RED

# 按值反查成员
print(Color(1))            # Color.RED
print(Color["RED"])        # Color.RED

# 遍历
for c in Color:
    print(c.name, c.value)     # RED 1 / GREEN 2 / BLUE 3
```

成员之间**判等**是安全的：

```python
Color.RED is Color.RED        # True
Color.RED == Color.RED        # True
Color.RED == 1                # False ← 和原始值不相等，这是优点
```

## 3. ⚠️ 普通 Enum 不能比较大小

> 普通 `Enum` **不支持大小比较**——成员之间没有「天然顺序」。

```python
Color.RED < Color.GREEN       # ❌ TypeError: '<' not supported
```

需要**排序/比较**时，改用 `IntEnum`：

```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3

Priority.LOW < Priority.HIGH          # True
sorted([Priority.HIGH, Priority.LOW]) # [Priority.LOW, Priority.HIGH]
Priority.HIGH == 3                    # True ← IntEnum 和整数等价
```

> 另外还有 `IntFlag`（可做位运算，适合权限组合）、`StrEnum`（值为字符串）。

## 4. 什么时候用枚举（速查）

> 当你写下任何一段「**这个变量只能取下面这几个值**」的代码时，就应该考虑 `Enum`。

| 场景 | 例子 |
| --- | --- |
| 状态机的状态 | `Pending` / `Running` / `Done` / `Failed` |
| 类别 / 类型 | 颜色、性别、文件类型 |
| 优先级 / 等级 | 用 `IntEnum`，可以排序和比较 |

**替代这种散落的魔法值**：

```python
# ❌ Before
STATUS_PENDING = 0
STATUS_RUNNING = 1
STATUS_DONE = 2

# ✅ After
class Status(Enum):
    PENDING = 0
    RUNNING = 1
    DONE = 2
```

让代码更安全、更清晰。

## 5. 实用小技巧

```python
# 给成员加说明文字
class Status(Enum):
    PENDING = ("pending", "等待中")
    RUNNING = ("running", "运行中")

    def __init__(self, code, label):
        self.code = code
        self.label = label

print(Status.PENDING.label)    # 等待中
```

```python
# 强制值唯一（值重复会报错）
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    BLUE = 1        # ❌ ValueError: duplicate values found
```

## ⚠️ 易错点速记

1. 普通 `Enum` **不能比较大小**，要排序用 `IntEnum`
2. `Color.RED == 1` 是 `False`（Enum 成员不等于它的原始值）—— 这是特性不是 bug
3. 拼写错误会立刻 `AttributeError`，这正是你要的保护
4. 值重复默认会被当作**别名**吞掉；要禁止重复用 `@unique`
5. `IntFlag` 才能做位运算（`|`、`&`），普通 `Enum` 不行
6. 需要「人话描述」时，用 `__init__` 挂额外属性，别把说明塞进 value

## 🔗 关联

- 类与对象 → [15-类属性与实例属性](15-类属性与实例属性.md)
- 字典与常量组织 → [04-字典](04-字典.md)
- 原始截图 → [source/2026-10-19/A.md](../source/2026-10-19/A.md)（图 image34、image35）
