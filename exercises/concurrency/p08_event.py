# -*- coding: utf-8 -*-
"""第 8 题 · Event：发信号

对应章节：教学 03 →「5、线程间通信」

要做的事：
  1. worker()：先打印「worker：等信号」→ event.wait() → 打印「worker：收到信号，开工」
  2. main()：
       - 起 worker 线程
       - 主线程 sleep(2)
       - 打印「主线程：发信号」
       - event.set()
       - join()

你应该看到：先「等信号」，停 2 秒，然后「发信号」和「收到信号，开工」。

想一想：Event 和 Condition 有什么区别？
"""
import time
import threading

event = threading.Event()


def worker():
    # TODO: 打印「worker：等信号」→ event.wait() → 打印「收到信号，开工」
    raise NotImplementedError("实现 worker()")


def main():
    # TODO: 起 worker → sleep(2) → 打印「主线程：发信号」→ event.set() → join
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
