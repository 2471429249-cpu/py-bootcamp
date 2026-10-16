# -*- coding: utf-8 -*-
"""练习 03：摄氏 / 华氏温度换算

练习点：
- 函数、参数与返回值
- 数学公式直接写成代码
- 格式化输出（保留小数位）
"""


def c_to_f(celsius):
    """摄氏 → 华氏"""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """华氏 → 摄氏"""
    return (fahrenheit - 32) * 5 / 9


def main():
    print("温度换算")
    print("1) 摄氏 → 华氏")
    print("2) 华氏 → 摄氏")
    choice = input("请选择（1/2）：").strip()

    if choice == "1":
        c = float(input("输入摄氏温度："))
        print(f"{c}°C = {c_to_f(c):.2f}°F")
    elif choice == "2":
        f = float(input("输入华氏温度："))
        print(f"{f}°F = {f_to_c(f):.2f}°C")
    else:
        print("无效选择")


if __name__ == "__main__":
    main()
