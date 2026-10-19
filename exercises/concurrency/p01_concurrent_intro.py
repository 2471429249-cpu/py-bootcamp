# -*- coding: utf-8 -*-
"""题 01 · 并发初体验：串行 vs 并发

目标：亲眼看到「并发 ≠ 更快，而是不用干等」。
要求：
  1. work(name, seconds) 打印 start → sleep → 打印 end
  2. 串行跑 3 次（各 1 秒），用 time.perf_counter() 计时
  3. 3 个线程并发跑，计时并打印总耗时
预期：串行约 3 秒；并发约 1 秒。
自测：sleep 时 CPU 在忙吗？把 sleep 换成纯计算，并发还会是 1 秒吗？
"""
import time
import threading


def work(name, seconds):
    """打印开始 → 睡 seconds 秒 → 打印结束。"""
    # TODO: 实现
    raise NotImplementedError("实现 work()")


def main():
    # TODO 1: 串行调用 3 次，计时
    # TODO 2: 3 个 threading.Thread 并发，计时
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
