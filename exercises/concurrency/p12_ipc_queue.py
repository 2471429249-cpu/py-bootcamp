# -*- coding: utf-8 -*-
"""第 12 题 · 进程之间用 Queue 通信

对应章节：教学 04 →「6、进程间通信」

要做的事：
  1. sender(q)：q.put("来自子进程的消息") → sleep(1)
  2. main()（在 __main__ 保护里）：
       q = multiprocessing.Queue()
       p = Process(target=sender, args=(q,))
       p.start()
       p.join()
       打印「主进程收到：」+ q.get()

你应该看到：主进程打印出「主进程收到：来自子进程的消息」。

注意：要用 multiprocessing.Queue()，不是 queue.Queue()。

想一想：结合第 10 题，为什么进程之间不能直接改全局变量？
"""
import time
import multiprocessing


def sender(q):
    # TODO: q.put("来自子进程的消息") → sleep(1)
    raise NotImplementedError("实现 sender()")


def main():
    # TODO: 建 Queue → 起 sender 进程 → start → join → 打印 q.get()
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
