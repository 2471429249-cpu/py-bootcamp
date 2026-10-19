---
title: 元类与 type
category: 进阶
keywords: [元类, metaclass, type, 一切类都源自type, 动态造类, 类也是对象, __init_subclass__]
dates: [2026-10-19]
---

# 元类与 type

> 一句话：**一切对象都源自类，一切类都源自 `type`**——类本身也是对象，它的"类"就是 `type`；元类就是"造类的类"。

## 1. 一切东西都是对象

> 一切对象都源自类，一切类都源自 `type`。

```python
class Dog:
    pass

d = Dog()

type(d)          # <class '__main__.Dog'>   ← 实例的类型是 Dog
type(Dog)        # <class 'type'>           ← 类的类型是 type！
type(type)       # <class 'type'>           ← type 自己也是 type
```

> `type()` 一个对象时返回它的类型。所以**所有 class 的类型都是 `type`**。

## 2. `type()` 的第二种用法：传三个参数造类

既然 `type` 是创建类的元类，那能不能**直接调用 `type` 来造一个类**？答案是能。

`type()` 还有第二种用法——传三个参数：

```python
type(类名, 父类元组, 属性字典)
```

| 参数 | 说明 |
| --- | --- |
| 类名 | 字符串，例如 `'Hello'` |
| 父类元组 | 单父类要写成单元组：`(object,)`，多继承就多个 |
| 属性字典 | `{'方法名': 函数, '属性名': 值}` |

### 等价写法对照

```python
# 写法一：class 语句（最常用）
class Hello:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")


# 写法二：type() 动态造类（与上面完全等价）
def __init__(self, name):
    self.name = name

def greet(self):
    print(f"Hello, {self.name}")

Hello2 = type("Hello2", (object,), {
    "__init__": __init__,
    "greet": greet,
    "version": 1,          # 类属性也一起放进来
})

h = Hello2("小明")
h.greet()                  # Hello, 小明
```

> 注意：`type()` 的第三个参数**就是类属性的字典**——所以你笔记里写的
> 「写在 `type()` 的字典里，或直接写在 `class` 下的：是类属性」说的就是同一件事。

## 3. 什么是元类

**元类 = 创建类的类**。`class` 语句在底层其实是一次元类调用：

```python
class Dog:                 # 大致相当于：
    pass                   # Dog = type("Dog", (object,), {})
```

自定义元类，就是**继承 `type`**、在"造类"时插一脚：

```python
class CheckNames(type):
    def __new__(mcs, name, bases, namespace):
        # 造类之前可以做检查：所有属性名必须小写
        for key in namespace:
            if key.startswith("__"):
                continue
            if key != key.lower():
                raise TypeError(f"属性名必须小写：{key}")
        return super().__new__(mcs, name, bases, namespace)


class Good(metaclass=CheckNames):
    speed = 10              # ✅

class Bad(metaclass=CheckNames):
    Speed = 10              # ❌ TypeError: 属性名必须小写：Speed
```

> 用你自己的话说：**元类的创立是一个中转站**——你建立一个类时，需要经过它，
> 并按它的要求被迫修改。

## 4. 元类的实际用途

| 用途 | 说明 |
| --- | --- |
| 强制命名 / 结构规范 | 上面的 `CheckNames`，团队代码规范自动检查 |
| 自动注册 | ORM、插件系统：定义类时自动登记到注册表 |
| 单例模式 | 控制"这个类只能有一个实例" |
| 自动加方法 | 给所有子类统一注入日志、序列化等方法 |

**自动注册**示例（最实用的一种）：

```python
REGISTRY = {}

class Register(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:                     # 跳过基类本身
            REGISTRY[name] = cls
        return cls


class Base(metaclass=Register):
    pass

class EmailSender(Base):     # 定义即注册
    pass

print(REGISTRY)              # {'EmailSender': <class 'EmailSender'>}
```

## 5. 大多数情况：别用元类，用 `__init_subclass__`

元类难懂、难调试。**90% 的场景**用下面这个更简单的钩子就够：

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        REGISTRY[cls.__name__] = cls      # 子类定义时自动执行


class EmailSender(Base):     # 定义即注册，不需要元类
    pass
```

> **经验法则**：能用 `__init_subclass__` / 类装饰器解决的，就不要上元类。

## ⚠️ 易错点速记

1. `type(Dog)` 是 `type`，不是 `Dog`——**类也是对象**
2. `type()` 单参数查类型；**三参数才是造类**
3. `type()` 的父类元组必须写成元组：单父类是 `(object,)`，**末尾逗号不能省**
4. 元类里 `__new__` 的第一参数是 `mcs`（元类自己），不是 `self`
5. `metaclass=` 会影响**所有子类**，别在别人的继承链上乱挂
6. 先考虑 `__init_subclass__` / 类装饰器，最后才考虑元类

## 🔗 关联

- 类属性与实例属性 → [15-类属性与实例属性](15-类属性与实例属性.md)
- 特殊方法与哈希 → [13-特殊方法与哈希](13-特殊方法与哈希.md)
- 原始截图 → [source/2026-10-19/A.md](../source/2026-10-19/A.md)（图 image36、手写要点 3、4、7）
