---
title: while 循环与真假值
category: 基础结构
keywords: [while, 循环, 真值, 假值, truthy, falsy, 布尔, match, case, 条件分支]
dates: [2026-10-18]
---

# while 循环与真假值

> 一句话：`while` 就是「**当条件为真时，就一直重复**」；而"真"和"假"远不止 `True`/`False` 两个值。

## 1. `while` 的基本形状

```python
count = 0
while count < 3:      # 条件为真 → 进循环
    print(count)
    count += 1        # 一定要让条件有机会变假，否则死循环
# 输出：0 1 2
```

配合 `break` / `continue`：

```python
while True:           # 最常见的写法：先无条件循环
    answer = input("输入 q 退出：")
    if answer == "q":
        break         # 唯一的出口
```

## 2. 「真值 / 假值」速查表

Python 里**任何对象**都能判断真假。只有下面这些是**假**，其它全是**真**：

| 类型 | 假值 |
| --- | --- |
| 数字 | `0`、`0.0` |
| 字符串 | `''` |
| 容器 | `[]`、`()`、`{}`、`set()` |
| 特殊 | `None`、`False` |

```python
while []:      # 假 → 一次都不执行
while "abc":   # 真 → 无限循环（别真这么写）
```

> 这在 `while` / `if` 里非常实用：判断"列表空没空"直接 `while items:` 就行，不用写 `while len(items) > 0:`。

## 3. `while` 还是 `for`？

| 场景 | 选哪个 |
| --- | --- |
| 遍历一个容器 / 已知次数 | `for` |
| 不知道要循环几次，靠条件停 | `while` |
| 用户输入直到满足条件 | `while True` + `break` |

## 4. 补充：`match / case` 该不该用

> 💡 `match / case` **不是用来取代** `if / elif` 的。

- **简单的值比较** → 写 `if` 反而更清楚
- **要根据「数据的结构」分发逻辑**（如解析 JSON / 处理 AST）→ `match` 才真正发挥威力

```python
# 好钢用在刀刃上：按「结构」分发
match event:
    case {"type": "click", "x": x, "y": y}:
        handle_click(x, y)
    case {"type": "key", "key": k}:
        handle_key(k)
```

## ⚠️ 易错点速记

1. `while` 里忘了改变条件变量 → **死循环**（Ctrl+C 可以中断）
2. `0`、`''`、`[]`、`{}`、`None` 都是假，别以为是"有值"
3. `while True:` 必须有 `break`，否则永远出不去
4. `match/case` 别拿来当 `if/elif` 的替代品，简单判断用 `if` 更可读

## 🔗 关联

- 条件与循环基础 → [01-函数与程序入口](01-函数与程序入口.md)
- 迭代器（`for` 背后是什么）→ [12-迭代器与enumerate](12-迭代器与enumerate.md)
- 原始截图 → [source/2026-10-18/A.md](../source/2026-10-18/A.md)（图 image26、image27）
