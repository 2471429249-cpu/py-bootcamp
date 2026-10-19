# -*- coding: utf-8 -*-
"""第 10 题 · 进程的内存是独立的

对应章节：教学 02「线程」+ 教学 04「进程间通信」

要做的事（两个实验，之间都要把 x 重置为 0）：
  实验 A（进程）：
       p = Process(target=set_x) → start → join → 主进程打印 x
  实验 B（线程）：
       t = Thread(target=set_x) → start → join → 主线程打印 x

其中 set_x() 就是：
       global x
       x = 1

你应该看到：
  实验 A → 0
  实验 B → 1

想一想：同样改成 1，为什么进程看不到、线程看得到？
"""
import threading
import multiprocessing

x = 0


def set_x():
    global x
    x = 1


def main():
    global x

    # TODO 实验 A：x = 0 → Process 跑 set_x → join → 打印 x
    # TODO 实验 B：x = 0 → Thread 跑 set_x → join → 打印 x
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
