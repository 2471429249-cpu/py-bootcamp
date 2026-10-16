# -*- coding: utf-8 -*-
"""练习 02：简易计算器

练习点：
- 函数定义与调用
- input() 读取输入、float()/int() 类型转换
- 条件分支（if/elif/else）
- 用字典做「运算符 → 函数」的分派（比一堆 if 更简洁）
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    print("简易计算器（支持 + - * /）")
    a = float(input("请输入第一个数："))
    op = input("请输入运算符（+ - * /）：").strip()
    b = float(input("请输入第二个数："))

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops:
        print("不支持的运算符")
        return
    if op == "/" and b == 0:
        print("除数不能为 0")
        return

    result = ops[op](a, b)
    print(f"结果：{a} {op} {b} = {result}")


if __name__ == "__main__":
    main()
