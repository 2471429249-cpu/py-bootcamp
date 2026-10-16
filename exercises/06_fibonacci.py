# -*- coding: utf-8 -*-
"""练习 06：斐波那契数列

练习点：
- 列表与循环的迭代写法
- 进阶：生成器函数 yield（惰性计算，不一次性占内存）
"""


def fib_list(n):
    """迭代法：返回前 n 项（n >= 1）"""
    if n <= 0:
        return []
    result = [0, 1]
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result[:n]


def fib_gen(n):
    """生成器版本：逐个 yield 前 n 项"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    n = 10
    print(f"前 {n} 项（列表法）：{fib_list(n)}")

    print("前 10 项（生成器法）：", end=" ")
    print(list(fib_gen(10)))


if __name__ == "__main__":
    main()
