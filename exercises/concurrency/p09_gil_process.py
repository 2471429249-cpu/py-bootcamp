# -*- coding: utf-8 -*-
"""题 09 · GIL 实测：线程 vs 进程（核心认知题）

写一个 CPU 密集函数：
    def cpu_work(n):
        s = 0
        for i in range(n):
            s += i * i
        return s

用 n = 20_000_000，跑 4 份，分别测总耗时：
  1. 串行：连续调用 4 次
  2. 4 线程：threading.Thread
  3. 4 进程：multiprocessing.Process

打印加速比 = 串行耗时 ÷ 并发耗时。

预期（实测，32 核机器）：
    串行   5.09s   1.00x
    4 线程 5.06s   1.01x   ← 等于没加速
    4 进程 1.61s   3.16x   ← 接近 4 核

⚠️ 进程版必须写在 if __name__ 保护里，否则 Windows 会无限开进程。

自测：
  1. 为什么 4 个线程没比串行快？
  2. 为什么进程能快？
  3. 那多线程还有什么用？（提示：I/O 密集）
"""
import time
import threading
import multiprocessing as mp


def cpu_work(n):
    """CPU 密集：返回 sum(i*i)。"""
    # TODO
    raise NotImplementedError("实现 cpu_work()")


def run_serial(n, times):
    # TODO: 串行跑 times 次，返回总耗时
    raise NotImplementedError("实现 run_serial()")


def run_threads(n, times):
    # TODO: times 个线程并发，返回总耗时
    raise NotImplementedError("实现 run_threads()")


def run_processes(n, times):
    # TODO: times 个进程并发，返回总耗时
    raise NotImplementedError("实现 run_processes()")


def main():
    print("cpu_count:", mp.cpu_count())
    n = 20_000_000
    times = 4
    # TODO: 依次测三种方式，打印耗时和加速比
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
