# -*- coding: utf-8 -*-
"""第 1 题 · 创建第一个线程

对应章节：教学 03 →「1、线程的创建」

要做的事：
  1. hello() 里：sleep(1) → 打印「子线程：我醒了」
  2. main() 里：创建 Thread(target=hello) → start()
  3. 紧接着打印「主线程：我结束了」

你应该看到：主线程那句先出现，1 秒后才出现子线程那句。

想一想：把 start() 改成 run() 会怎样？
"""
import time
import threading


def hello():
    # TODO: 先 sleep(1)，再打印「子线程：我醒了」
    raise NotImplementedError("实现 hello()")


def main():
    # TODO: 创建线程 → start() → 打印「主线程：我结束了」
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
