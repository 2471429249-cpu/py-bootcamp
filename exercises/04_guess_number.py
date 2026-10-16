# -*- coding: utf-8 -*-
"""练习 04：猜数字游戏

练习点：
- import 使用标准库 random
- while True 死循环 + break 退出
- 比较运算、计数器变量
- 异常处理（输入不是数字时不让程序崩溃）
"""

import random


def main():
    target = random.randint(1, 100)  # 1~100 随机整数
    tries = 0
    print("我已经想好了一个 1~100 之间的数，来猜吧！")

    while True:
        raw = input("你猜多少：").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("请输入一个整数")
            continue

        tries += 1
        if guess < target:
            print("小了，再大一点")
        elif guess > target:
            print("大了，再小一点")
        else:
            print(f"恭喜！就是 {target}，你共猜了 {tries} 次")
            break


if __name__ == "__main__":
    main()
