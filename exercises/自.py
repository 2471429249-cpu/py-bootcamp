#1
"""
a=3
b=7
print(f"交换前：a = {a},b={b}")
a,b=b,a
print(f"jiaohuanhuo:a={a},b={b}")

#2
def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a//b

def main():
    print("jisuan")
    a = float(input("第一个数："))
    fu = input("运算符：")
    b= float(input("第二个数字"))
    if fu == "+":
        print(jia(a,b))
    elif fu == "-":
        print(jian(a,b))
    elif fu == "*":
        print(cheng(a,b))
    elif fu == "/":
        print(chu(a,b))


if __name__ == "__main__":
    main()

def change1(c):
    return c*(9/5)+32
def change2(f):
    return (f-32)*5/9
def main():
    x =int(input("object"))
    if x==1:
        c=float(input("转华氏度"))
        print(change1(c))
    elif x==2:
        f=float(input("object"))
        print(change2(f))
    else :
        print("error")
if __name__ == "__main__":
    main()
"""
import random

def rand():
    x = random.randint(1,100)
    tryies =0
    while True:
        a = int(input())
        tryies += 1
        if a == x:






