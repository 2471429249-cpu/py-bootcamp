# -*- coding: utf-8 -*-
"""第 9 题 · 创建第一个进程

对应章节：教学 04 →「1、类 Process」

要做的事：
  1. worker(name)：打印「子进程 {name} 的 PID：{os.getpid()}」→ sleep(1) → 打印结束
  2. main()（在 __main__ 保护里）：
       - 打印「主进程 PID：{os.getpid()}」
       - 创建两个 Process：args=("A",) 和 ("B",)
       - 都 start()，再都 join()
       - 打印「全部结束」

你应该看到：3 个不同的 PID，且「全部结束」在最后。

想一想：为什么 Windows 必须写 if __name__ == "__main__"？（删掉试试）
"""
import os
import time
import multiprocessing


def worker(name):
    # TODO: 打印子进程 name + PID → sleep(1) → 打印结束
    raise NotImplementedError("实现 worker()")


def main():
    # TODO: 打印主进程 PID → 创建 2 个进程 → start → join → 打印「全部结束」
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
