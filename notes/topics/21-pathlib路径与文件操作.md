---
title: pathlib 路径与文件操作
category: 工程
keywords: [pathlib, Path, 路径, 文件操作, read_text, write_text, glob, mkdir, exists, unlink]
dates: [2026-10-21]
---

# pathlib 路径与文件操作

> 一句话：**路径在 pathlib 里不是字符串，而是一个有属性、有方法的"对象"**——用 `Path` 代替 `os.path` 的字符串拼接。

## 1. 综合演示：路径拆解

```python
from pathlib import Path

p = Path('/Users/walter/projects/demo/main.py')

print('name  :', p.name)      # main.py
print('stem  :', p.stem)      # main
print('suffix:', p.suffix)    # .py
print('parent:', p.parent)    # /Users/walter/projects/demo
print('parts :', p.parts)     # ('/', 'Users', 'walter', 'projects', 'demo', 'main.py')
```

`.parts` 把整个路径切成元组，逐段处理特别方便。

## 2. 判断状态（防报错必用）

```python
p = Path('/tmp')
print(p.exists())     # 路径是否存在
print(p.is_dir())     # 是不是目录
print(p.is_file())    # 是不是文件
```

| 方法 | 作用 | 白话 |
| --- | --- | --- |
| `.exists()` | 判断路径是否存在 | 到底有没有这个东西（不管文件还是文件夹） |
| `.is_file()` | 判断是不是文件 | 这是一个文件吗（`.txt`、`.py`） |
| `.is_dir()` | 判断是不是目录 | 这是一个文件夹吗 |

## 3. 读写文件（极简版）

```python
p = Path('demo.txt')

p.write_text('你好', encoding='utf-8')    # 一行写完；不存在会自动创建，存在会覆盖
content = p.read_text(encoding='utf-8')   # 一行读完全部，返回字符串
```

> ⚠️ **千万记得写 `encoding='utf-8'`**，否则中文在 Windows 上容易乱码。

## 4. 找文件（遍历目录）

| 方法 | 作用 | 白话 |
| --- | --- | --- |
| `.iterdir()` | 列出下一层 | 看看这个文件夹里都有啥（只找第一层，不往子文件夹钻） |
| `.glob('*.py')` | 找匹配的文件 | 在当前文件夹里找所有 `.py` 文件 |
| `.rglob('*.py')` | 递归找匹配的文件 | 在当前及所有子文件夹里，掘地三尺找 `.py` |

```python
for f in Path('.').glob('*.py'):
    print(f.name)

for f in Path('.').rglob('*.py'):    # r = recursive 递归
    print(f)
```

## 5. 创建与删除

| 方法 | 作用 | 口语解释 |
| --- | --- | --- |
| `.mkdir(parents=True, exist_ok=True)` | 建文件夹 | `parents=True`：父文件夹不存在自动帮你建（类似 `mkdir -p`）；`exist_ok=True`：已经存在了不报错 |
| `.touch()` | 建空文件 | 摸一下，建一个空文件；已存在就只更新修改时间 |
| `.unlink(missing_ok=True)` | 删文件 | `missing_ok=True`：要删的文件本来就不存在，别报错 |

```python
Path('data/2026').mkdir(parents=True, exist_ok=True)
Path('demo.txt').touch()
Path('demo.txt').unlink(missing_ok=True)
```

## 6. 附赠常用属性（无括号）

| 属性 | 作用 | 例子 |
| --- | --- | --- |
| `.name` | 文件名（含后缀） | `demo.txt` |
| `.stem` | 文件名（无后缀） | `demo` |
| `.suffix` | 文件后缀 | `.txt` |
| `.parent` | 父目录 | 这个文件在哪个文件夹里 |
| `.absolute()` | 绝对路径 | 从盘符/根目录开始的完整路径 |

```python
print(Path.home())       # 当前用户的家目录
print(Path.cwd())        # 当前工作目录
Path('a/b.txt').absolute()   # 变成绝对路径
```

## 7. 🔑 老手实战口诀（背下来）

1. **读写文件一律带** `encoding='utf-8'`
2. **建文件夹一律带** `parents=True, exist_ok=True`
3. **删文件一律带** `missing_ok=True`
4. 只要带 `ok=True` 这类参数，就能让你**免去 80% 的"文件已存在"或"文件找不到"的崩溃报错**

## ⚠️ 易错点速记

1. `Path` 是对象，不能直接和字符串拼——用 `/` 运算符：`Path('a') / 'b.txt'`
2. 读写文本**必须** `encoding='utf-8'`，否则中文乱码
3. `.mkdir()` 不加 `parents=True` 时，父目录不存在会报错
4. `glob` 只找当前层，`rglob` 才会递归
5. 属性（`.name`/`.parent`）**没有括号**；方法（`.exists()`）**有括号**
6. 想兼容不同系统路径分隔符，就全程用 `Path`，别手写 `\\` 或 `/`

## 🔗 关联

- 文件读写基础（`open` / `with`）→ 待建专题
- 异常处理（`FileNotFoundError`）→ [22-异常处理](22-异常处理.md)
- 原始截图 → [source/2026-10-21/A.md](../source/2026-10-21/A.md)（图 image60~image63）
