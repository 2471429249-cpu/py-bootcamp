# -*- coding: utf-8 -*-
"""题 10 · Pool 进程池：批量开进程

task(name)：打印进程名 + PID → sleep(0.5) → 打印耗时。

1. 用 Pool(4) 提交 6 个任务（apply_async）
2. 正确收尾：先 p.close() 再 p.join()
3. 再改成 Pool(6) 跑一次，对比总耗时

预期：
  Pool(4) → 0/1/2/3 立刻开始，4/5 等槽位；总耗时约 1 秒
  Pool(6) → 6 个一起跑，总耗时约 0.5 秒

关键：close() 之前可以继续提交任务；close() 之后不行；join() 必须在 close() 之后。

自测：
  1. Pool(4) 里同时最多跑几个任务？
  2. apply 和 apply_async 的区别？
"""
import os
import time
from multiprocessing import Pool


def task(name):
    # TODO: 打印进程名/PID → sleep(0.5) → 打印本任务耗时
    raise NotImplementedError("实现 task()")


def main():
    # TODO: Pool(4) 跑 6 个任务，close + join，打印总耗时
    # TODO: 再试 Pool(6) 对比
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
