# -*- coding: utf-8 -*-
"""第 7 题 · Queue：线程之间传数据

对应章节：教学 03 →「5、线程间通信」

要做的事：
  1. main() 里创建 q = Queue()
  2. writer()：依次 put "苹果"、"香蕉"、"橘子"，最后 put(None)
  3. reader()：while True: v = q.get()；v 是 None 就 break，否则打印「读到：v」
  4. 起两个线程，start 后都 join

你应该看到：三行「读到：苹果/香蕉/橘子」，然后程序正常结束。

想一想：那个 None 是干什么用的？
"""
import threading
from queue import Queue


def writer(q):
    # TODO: put 三个水果名，最后 put(None)
    raise NotImplementedError("实现 writer()")


def reader(q):
    # TODO: while True 里 get()，None 就 break，否则打印
    raise NotImplementedError("实现 reader()")


def main():
    # TODO: 建 Queue → 起 writer 和 reader 两个线程 → start → join
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
