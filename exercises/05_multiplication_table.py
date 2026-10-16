# -*- coding: utf-8 -*-
"""练习 05：九九乘法表

练习点：
- 嵌套 for 循环
- range(1, 10) 的边界（左闭右开）
- print 的 end 参数（不换行）、格式化对齐
"""


def main():
    for i in range(1, 10):          # 行：1~9
        for j in range(1, i + 1):   # 列：1~i（下三角）
            # :<3 表示左对齐、占 3 个字符宽度，让表整齐
            print(f"{j}×{i}={i * j:<3}", end="  ")
        print()  # 每行结束换行


if __name__ == "__main__":
    main()
