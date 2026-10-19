# -*- coding: utf-8 -*-
"""第 3 题 · join：让主线程等一等

对应章节：教学 03 →「2、线程合并（join 方法）」

在第 1 题基础上，只加 1 行：
  1. 创建线程 t（跑 hello）
  2. t.start()
  3. t.join()          ← 就是这一行
  4. 打印「主线程：我结束了」

你应该看到：顺序反过来 —— 先「子线程：我醒了」，后「主线程：我结束了」。

想一想：join() 阻塞的是哪个线程？
"""
import time
import threading


def hello():
    time.sleep(1)
    print("子线程：我醒了")


def main():
    t = threading.Thread(target=hello)
    # TODO: start() 之后调用 t.join()，再打印「主线程：我结束了」
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
