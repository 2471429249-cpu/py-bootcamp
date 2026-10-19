# -*- coding: utf-8 -*-
"""题 11 · 进程间通信：为什么进程不能用普通变量

(a) multiprocessing.Queue 版
    主进程创建 q，两个子进程：一个写 3 个值，一个循环读并打印。
    收尾：写进程 join()；读进程是死循环，只能 terminate()。

(b) 反例实验（很重要）
    把 Queue 换成【普通全局 list】，主进程里放 3 个元素，子进程打印这个 list。
    观察子进程打印出什么。

预期：
  (a) 能读到 3 个值（顺序可能交错），程序正常退出
  (b) 子进程看到的是【空列表】→ 证明进程内存不共享

自测：
  1. 为什么进程之间不能共享普通全局变量？
  2. Queue 和 Pipe 的区别？
  3. 为什么这里对读进程用 terminate() 而不是 join()？
"""
import os
import random
import time
from multiprocessing import Process, Queue


def writer(q):
    # TODO: 往 q 里写 3 个值（中间可 sleep 一下）
    raise NotImplementedError("实现 writer()")


def reader(q):
    # TODO: while True: q.get() 并打印
    raise NotImplementedError("实现 reader()")


def part_a():
    """Queue 版。"""
    # TODO: 建 Queue → 起两个进程 → join 写进程 → terminate 读进程
    raise NotImplementedError("实现 part_a()")


def part_b():
    """反例：普通 list 在子进程里是空的。"""
    # TODO
    raise NotImplementedError("实现 part_b()")


def main():
    # TODO: 先跑 (a) 再跑 (b)
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
