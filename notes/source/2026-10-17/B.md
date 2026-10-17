# Python 学习笔记截图转写（B 组：note21、note22、note24、note26、note28、note29）

> 说明：以下按截图原样转写，代码逐字保留（含缩进、括号、引号、运算符）。图片为深色/浅色代码块截图，代码块标签与按钮等界面元素在需要处用括号说明。

## 图 note21

知识点：字符串反转的两种写法——切片步长 `-1` 与 `reversed()` 配合 `join()`。

（深色主题代码块，无标题文字，共两个方法示例）

```python
# 方法 1：切片步长 -1
print("切片反转：", s[::-1])

# 方法 2: reversed + join
print("reversed: ", "".join(reversed(s)))
```

## 图 note22

知识点：用生成器函数 `fib_gen` 逐个 `yield` 出斐波那契数列的前 n 项。

（深色主题代码块。注意：`def` 行右边那句「1 个用法」是编辑器/IDE 内联显示的用法计数提示，不属于代码内容。）

```python
def fib_gen(n):
    """生成器版本: 逐个 yield 前 n 项"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

## 图 note24

知识点：`main(a, b)` 的两个形参之所以「多余」，是因为函数体一上来就用 `input()` 把 `a`、`b` 重新赋值覆盖了，传进来的值根本没被用到。

### 一、main(a, b) 里的参数为什么多余

先看你原来的 `main` 定义：

（代码块标签：python；右上角按钮：复制、下载）

```python
def main(a, b):                     # ① 定义时要求传 2 个参数
    print("jisuan")
    a = float(input("第一个数："))   # ② 立刻把 a 覆盖了
    fu = input("运算符：")
    b = float(input("第二个数字"))   # ③ 立刻把 b 覆盖了
    ...
```

### 问题出在哪

调用 `main(a, b)` 时，外面的 `a`、`b` 会先传进去。但函数体第 ②③ 行马上：

（代码块标签：python；右上角按钮：复制、下载）

```python
a = float(input(...))    # 重新赋值
b = float(input(...))    # 重新赋值
```

传进来的值根本没被用上，立刻被 `input()` 覆盖。

### 举例说明

（代码块标签：python；右上角按钮：复制、下载）

```python
def main(a, b):
    a = 100
    b = 200
    print(a, b)

main(1, 2)       # 输出 100 200
main(999, 888)   # 还是输出 100 200
```

传什么进去都一样，因为里面改掉了。那这个参数就等于白写。

## 图 note26

知识点：用 `type()` 函数可以查看变量的数据类型。

这里我们可以使用 `type()` 函数来查看下类型。

## 图 note28

知识点：在 f-string 中用 `:,` 格式说明符给数字加千分位逗号。

数字加千分位逗号：

（代码块标签：PYTHON）

```python
amount = 1234567890

print(f'订单金额：{amount:,} 元')
```

## 图 note29

知识点：Python 基本数据类型转换函数一览（int / float / complex / str / repr / eval / tuple / list / chr / ord / hex / oct）。

Python 中基本数据类型转换的方法有下面几个。

| 方法 | 说明 |
| --- | --- |
| int(x [,base ]) | 将x转换为一个整数 |
| float(x ) | 将x转换到一个浮点数 |
| complex(real [,imag ]) | 创建一个复数 |
| str(x ) | 将对象 x 转换为字符串 |
| repr(x ) | 将对象 x 转换为表达式字符串 |
| eval(str ) | 用来计算在字符串中的有效 Python 表达式,并返回一个对象 |
| tuple(s ) | 将序列 s 转换为一个元组 |
| list(s ) | 将序列 s 转换为一个列表 |
| chr(x ) | 将一个整数转换为一个字符 |
| ord(x ) | 将一个字符转换为它的整数值 |
| hex(x ) | 将一个整数转换为一个十六进制字符串 |
| oct(x ) | 将一个整数转换为一个八进制字符串 |

注：在 Python 3 里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
