# -*- coding: utf-8 -*-
"""第 11 题 · Pool 进程池

对应章节：教学 04 →「5、Pool」

要做的事：
  1. task(name)：打印「任务 {name} 开始，PID：{os.getpid()}」→ sleep(1) → 打印结束
  2. main()（在 __main__ 保护里）：
       p = Pool(2)
       用 p.apply_async(task, args=(i,)) 提交 4 个任务（1,2,3,4）
       p.close()
       p.join()
       打印「全部结束」

你应该看到：任务 1、2 先跑；结束后 3、4 才开始；总耗时约 2 秒。

想一想：Pool(2) 最多同时跑几个？为什么 close() 要在 join() 前面？
"""
import os
import time
from multiprocessing import Pool


def task(name):
    # TODO: 打印开始 + PID → sleep(1) → 打印结束
    raise NotImplementedError("实现 task()")


def main():
    # TODO: Pool(2) → 提交 4 个任务 → close() → join() → 打印「全部结束」
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
