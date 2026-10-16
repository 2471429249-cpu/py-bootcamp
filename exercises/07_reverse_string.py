# -*- coding: utf-8 -*-
"""练习 07：字符串反转

练习点：
- 切片 [::-1]（Python 最优雅的反转写法）
- reversed() + "".join(
- 认识中文等 Unicode 字符在反转时也正确
"""


def main():
    s = "hello, 世界"

    # 方法 1：切片步长 -1
    print("切片反转：", s[::-1])

    # 方法 2：reversed + join
    print("reversed：", "".join(reversed(s)))


if __name__ == "__main__":
    main()
