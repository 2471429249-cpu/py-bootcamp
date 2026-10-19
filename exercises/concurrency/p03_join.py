# -*- coding: utf-8 -*-
"""题 03 · join：让主线程等一等

3 个子线程各 sleep(1) 后打印「[子线程 x] 结束」；
主线程最后打印「[主线程] 全部结束」。

要求跑两遍：
  第一遍：不加 join   → 观察主线程那句会先出现
  第二遍：加上 join   → 观察它变成最后出现

自测：
  1. join() 阻塞的是哪个线程？
  2. 为什么不能在 start() 之前 join()？
  3. t.join(timeout=2) 有什么用？
"""
import time
import threading


def worker(name):
    # TODO: sleep(1) 后打印「[子线程 x] 结束」
    raise NotImplementedError("实现 worker()")


def main():
    # TODO: 创建 3 个线程并 start()
    # TODO: 第一遍先不 join，跑一次看顺序
    # TODO: 第二遍加上 for t in threads: t.join()，再跑一次
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
