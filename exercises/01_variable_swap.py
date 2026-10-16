# -*- coding: utf-8 -*-
"""练习 01：变量交换

练习点：
- 变量与赋值
- Python 的「多重赋值」语法糖：a, b = b, a（底层是元组打包再解包）
"""


def main():
    a = 3
    b = 7
    print(f"交换前：a = {a}, b = {b}")

    # 一行完成交换，Python 特有的简洁写法
    a, b = b, a

    print(f"交换后：a = {a}, b = {b}")

    a, b = b, a
    print(f"a = {a}, b = {b}")

if __name__ == "__main__":
    main()
