# Python 学习笔记 · 截图转写（2026-10-21 新增部分）

> 来源：`py-bootcamp/新建 DOC 文档.doc`（累积文档，本次共 66 张截图）。前 55 张已在前四次转写完成，
> 本次新增 **11 张**（image56 ~ image66），**本次无手写正文，全部是截图**。
>
> 今日主题：**推导式 / 类型注解 / pathlib 路径与文件操作 / 异常处理**。

> 转写约定
> - 代码逐字保留：缩进、空行、符号、运算符、引号一律按原图照抄，不改写、不省略。
> - 表格、灰底行内代码（圆角浅灰底）、深色代码块按原样式还原为 Markdown 形式。
> - 图中被裁切的残缺行、语法高亮／下划线等排版差异，单独用「转写说明」标出，与正文内容区分。

---

## 图 image56

知识点：**推导式的通用结构** —— 一行把一个序列变成另一个序列。

2、推导式的通用结构

```text
[表达式 for 变量 in 可迭代对象 if 条件]
```

- **表达式**：每个元素被收集前要做什么变换（不变换就直接写变量名）
- **for … in**：遍历哪个序列
- **if**：可选过滤条件，不需要就省略

> **转写说明**：标题为「2、推导式的通用结构」。三段说明中「表达式」「for … in」「if」加粗；
> `[表达式 for 变量 in 可迭代对象 if 条件]` 为浅灰圆角底的行内代码块样式。

---

## 图 image57

知识点：**字典推导式** —— 结构是 `{键: 值 for 变量 in 可迭代对象}`。

字典推导式：

```python
prices = {'apple': 5, 'banana': 3, 'cherry': 10}
doubled = {k: v * 2 for k, v in prices.items()}
print(doubled)
```

结构：`{键: 值 for 变量 in 可迭代对象}`。

> **转写说明**：代码块左上角有 `PYTHON` 语言标签，右上角有「复制」「▶ 试运行」按钮。
> 末行结构与 `{键: 值 …}` 为浅灰圆角底行内代码样式。

---

## 图 image58

知识点：**为什么需要 `.items()`** —— 直接 `for` 只能拿到"键"，要同时拿键和值必须用 `.items()`。

1. 为什么需要 `.items()`？

如果你直接对字典用 `for` 循环，你只能拿到"键"：

```python
prices = {"apple": 5, "banana": 3}

for k in prices:
    print(k)  # 输出: apple, banana （只有键，拿不到价格）
```

如果你想同时拿到"名字"和"价格"，就必须用 `.items()`：

```python
for k, w in prices.items():  # 👈 注意这里的 k, w
    print(k, w)
# 输出：
# apple 5
# banana 3
```

- `.items()` 产生的东西长这样：`[('apple', 5), ('banana', 3)]`
- 当 `k, w` 遇到这种成对的数据时，Python 会自动把第一个元素给 `k`（键），第二个给 `w`（值）。这就叫**解包（unpacking）**。

> **转写说明**：标题为「1. 为什么需要 `.items()`？」。代码块中 `# 输出: apple, banana （只有键，拿不到价格）` 为浅色注释；
> 第二段代码注释里的 👈 是原图 emoji。末两句里 `.items()` 与 `k, w` 为行内代码样式，「解包（unpacking）」加粗。

---

## 图 image59

知识点：**类型注解的基本语法** —— 口诀「参数加冒号，返回加箭头」。

1、基本语法

记住这个口诀：「**参数加冒号，返回加箭头**」。

```python
def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f'你好，{name}'


def log(message: str) -> None:      # 没有返回值就写 None
    print(message)
```

> **转写说明**：标题为「1、基本语法」。术语「参数加冒号，返回加箭头」加粗并用引号括起。
> 代码块右上角有「复制」按钮；`-> None` 后的注释为浅色。三处函数定义之间各空两行。

---

## 图 image60

知识点：**pathlib 综合演示** —— 路径是「对象」不是字符串，可拆出 name/stem/suffix/parent/parts。

7、综合演示

```python
from pathlib import Path

p = Path('/Users/walter/projects/demo/main.py')

print('name  :', p.name)
print('stem  :', p.stem)
print('suffix:', p.suffix)
print('parent:', p.parent)
print('parts :', p.parts)
```

输出：

```text
name  : main.py
stem  : main
suffix: .py
parent: /Users/walter/projects/demo
parts : ('/', 'Users', 'walter', 'projects', 'demo', 'main.py')
```

最后一个 `.parts` 把整个路径切成元组，逐段处理特别方便。

是不是发现路径在 `pathlib` 里彻底**不是字符串**了——它是一个有属性、有方法的「对象」？

> **转写说明**：标题为「7、综合演示」。代码块右上角有「复制」「▶ 试运行」按钮。
> 末段 `pathlib` 为行内代码样式，「不是字符串」加粗。

---

## 图 image61

知识点：**判断文件 / 目录是否存在**。

1、判断文件 / 目录是否存在

```python
from pathlib import Path

p = Path('/tmp')
print(p.exists())     # 路径是否存在
print(p.is_dir())     # 是不是目录
print(p.is_file())    # 是不是文件
```

> **转写说明**：标题为「1、判断文件 / 目录是否存在」。代码块右上角有「复制」「▶ 试运行」按钮；
> 三行 `#` 后为浅色注释。

---

## 图 image62

知识点：**pathlib 文件系统操作速查表**（判断状态 / 读写 / 找文件 / 创建）。

📁 pathlib 文件系统操作速查表

### 一、判断状态（防报错必用）

| 关键词 | 作用 | 白话解释 |
| --- | --- | --- |
| `.exists()` | 判断路径是否存在 | 到底有没有这个东西？（不管它是文件还是文件夹） |
| `.is_file()` | 判断是不是文件 | 这是一个文件吗？（比如 `.txt`、`.py`） |
| `.is_dir()` | 判断是不是目录 | 这是一个文件夹吗？（比如 `/tmp`） |

### 二、读写文件（极简版）

| 关键词 | 作用 | 白话解释 |
| --- | --- | --- |
| `.read_text(encoding="utf-8")` | 一行读完文本 | 把文件里的字全部读出来变成一个字符串。**千万记得写 `utf-8`**。 |
| `.write_text('内容', encoding="utf-8")` | 一行写完文本 | 把内容写进文件。如果文件不存在会自动创建，如果存在会覆盖原内容。 |

### 三、找文件（遍历目录）

| 关键词 | 作用 | 白话解释 |
| --- | --- | --- |
| `.iterdir()` | 列出下一层 | 看看这个文件夹里都有啥（只找第一层，不往子文件夹里钻）。 |
| `.glob('*.py')` | 找匹配的文件 | 在当前文件夹里找所有 `.py` 文件。 |
| `.rglob('*.py')` | 递归找匹配的文件 | 在当前文件夹以及所有子文件夹里，掘地三尺找所有 `.py` 文件。 |

### 四、创建与删除

| 关键词 | 作用 | 白话解释 |
| --- | --- | --- |
| `.mkdir(parents=True, exist_ok=True)` | 建文件夹 | `parents=True`：如果父文件夹不存在，自动帮你建（类似 `mkdir -p`）。`exist_ok=True`：如果文件夹已经有了，别报错，装没看见就行。 |

> **转写说明**：本图底部有裁切（"四、创建与删除"表格的最后一行部分被截断），续图见 image63。
> 所有"关键词"列均为浅灰圆角底的行内代码样式；表头三列依次为「关键词」「作用」「白话解释」。

---

## 图 image63

知识点：**pathlib 续** —— `touch` / `unlink` / 常用属性 / 老手实战口诀。

| 关键词 | 作用 | 白话解释 |
| --- | --- | --- |
| `.touch()` | 建空文件 | 摸一下，建一个空文件。如果文件已存在，只更新修改时间。 |
| `.unlink(missing_ok=True)` | 删文件 | 删掉这个文件。`missing_ok=True`：如果要删的文件本来就不存在，别报错。 |

### 五、附赠常用属性（无括号）

| 属性 | 作用 | 白话解释 |
| --- | --- | --- |
| `.name` | 文件名 | 包含后缀，比如 `demo.txt` |
| `.stem` | 文件名（无后缀） | 比如 `demo` |
| `.suffix` | 文件后缀 | 比如 `.txt` |
| `.parent` | 父目录 | 这个文件在哪个文件夹里 |
| `.absolute()` | 绝对路径 | 从 C 盘 / 根目录开始算起的完整路径 |

💡 **老手实战口诀**：

1. 读写文件一律带 `encoding='utf-8'`。
2. 建文件夹一律带 `parents=True, exist_ok=True`。
3. 删文件一律带 `missing_ok=True`。
4. 只要带 `ok=True`，就能让你免去 80% 的"文件已存在"或"文件找不到"的崩溃报错。

> **转写说明**：本图接 image62 的「四、创建与删除」表。末段口诀前有 💡 图标；四条中所有参数为行内代码样式。
> 「老手实战口诀」加粗。

---

## 图 image64

知识点：**异常处理完整四件套的顺序** —— `try` → `except`（多个）→ `else` → `finally`。

完整四件套的顺序

```python
try:
    # 可能出错的代码
    pass
except SomeError:
    # 出错时怎么办
    pass
except AnotherError:
    # 多个 except
    pass
else:
    # 没出错的话执行
    pass
finally:
    # 不管出不出错，都要执行
    pass
```

顺序是固定的：`try` → `except`（多个）→ `else` → `finally`。`else` 和 `finally` 都是可选的，但写的话只能按这个顺序。

> **转写说明**：代码块右上角有「复制」按钮。末段 `try`、`except`、`else`、`finally` 均为浅灰圆角底行内代码样式。

---

## 图 image65

知识点：**Python 异常处理核心笔记**（长图速查表：四件套 / `raise` / 自定义异常 / 报错名清单 / 致命坑）。

> 图首注释：「这份笔记帮你把零星小知识串成了一条线。按照"语法结构"和"实战场景"分类，直接照做即可。」

🤖 **Python 异常处理核心笔记**

### 一、核心语法结构（四件套）

```python
try:
    # 1. 可能出错的代码（只放真正危险的那一行）
    result = 10 / x
except ZeroDivisionError as e:
    # 2. 错误发生时的执行（用 as 捕获具体错误）
    print(f"除零错误: {e}")
except (ValueError, KeyError):
    # 3. 捕获多种错误（类型名用括号括起来）
    print("数据错误")
except Exception as e:
    # 4. 万能兜底（捕获其他所有异常，但别乱用！）
    print(f"未知错误: {e}")
else:
    # 5. 没报错才走这里（用于"成功后的后续操作"）
    print(f"计算成功，结果: {result}")
finally:
    # 6. 无论报不报错都会执行（常用于关闭文件、释放资源）
    print("清理工作完成")
```

⚡ 铁律：写多个 `except` 时，**必须子类在前，父类在后**，否则父类会把子类全吃掉。

### 二、主动"扔"错：`raise`

| 项 | 说明 |
| --- | --- |
| 作用 | 当参数不合规、业务不满足时，主动引爆。 |
| 写法 | `raise ValueError("年龄不能为负")` |
| 好处 | 比 `return None` 清晰一万倍——调用方一看就知道是参数错了，而不是没有数据。 |
| 异常链（高级） | `raise 业务异常("消息") from e`（保留底层的原始错误，方便排查根因）。 |

### 三、自定义异常类

| 项 | 说明 |
| --- | --- |
| 怎么写 | `class MyError(Exception): pass`（**必须继承 `Exception`**）。 |
| 为什么要写 | 1. 同样的 `ValueError`，分不清是"年龄错了"还是"网络错了"。<br>2. 自定义异常可以搭成家族体系（父类抓全局，子类抓细节）。<br>3. 还能带数据（在 `__init__` 里塞 `user_id`、`time` 等）。 |

### 四、必背"报错名"清单（最常见的 8 个）

| 异常名 | 触发场景（大白话） |
| --- | --- |
| `ValueError` | 类型对了，但值不对（比如 `int("abc")`） |
| `TypeError` | 类型不对（比如 `"字符串" + 1`） |
| `KeyError` | 字典里找不到这个键 |
| `IndexError` | 列表越界（比如只有 3 个，非要拿第 4 个） |
| `AttributeError` | 对象没有这个属性（比如 `"abc".foo`） |
| `FileNotFoundError` | 找不着文件（路径写错了） |
| `ZeroDivisionError` | 数学上违规（除以 0） |
| `Exception` | 万能兜底，不知道具体错误时用它 |

（注：`KeyboardInterrupt` 和 `SystemExit` 不继承 `Exception`，抓了 `except Exception` 也抓不住 Ctrl+C 和 `sys.exit()`。）

### 五、老手 vs 新手的 3 个致命坑

1. **绝不要裸 `except`**。裸 `except` 会吞掉所有的无出错误（包括你想要的 Ctrl+C）全吞了。排查问题时大海捞针，至少写成 `except Exception as e`。
2. **绝不 `except Exception: pass`**。这叫"掩耳盗铃"。程序报错被悄悄吞掉，以后出了 Bug 神仙都救不回来。
3. **不要把无关代码塞进 `try`**。`try` 里的行数越多，报错的精确度越低。**尽量只包住那一句"危险动作"**。

> **转写说明**：本图为长图（390×1053 px），是手机端截图。图首有一行浅色小字注释。
> 各表格的"关键词"/"项"列与异常名为行内代码样式。第五节的编号 1/2/3 前有加粗的"绝不/绝不/不要"。
> 图底部有裁切。

---

## 图 image66

知识点：**自定义异常必须继承 `Exception`**。

你写了 `(Exception)`。在 Python 里，所有想用 `raise` 抛出的异常，**必须继承自 `Exception` 这个"老祖宗"**。如果不继承它，Python 不认这个异常，你 `raise` 的时候会直接报错。

> **转写说明**：`(Exception)`、`raise`、`Exception` 均为浅灰圆角底行内代码样式；
> 「必须继承自 `Exception` 这个"老祖宗"」中"必须继承自"加粗。

---

## 本次涉及的专题

| 专题 | 对应截图 |
| --- | --- |
| [19-推导式](../../topics/19-推导式.md) | image56、image57 |
| [04-字典](../../topics/04-字典.md)（`.items()` 补充） | image58 |
| [20-类型注解](../../topics/20-类型注解.md) | image59 |
| [21-pathlib路径与文件操作](../../topics/21-pathlib路径与文件操作.md) | image60 ~ image63 |
| [22-异常处理](../../topics/22-异常处理.md) | image64 ~ image66 |
