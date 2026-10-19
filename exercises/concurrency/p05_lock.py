# -*- coding: utf-8 -*-
"""第 5 题 · 用 Lock 保护共享计数器（最重要的一题）

对应章节：教学 03 →「3、线程同步与互斥锁」

要做的事：
  1. add() 循环 20 次，每次三行：
         tmp = counter
         time.sleep(0.001)
         counter = tmp + 1
  2. main()：4 个线程都跑 add → 全部 start → 全部 join → 打印 counter
  3. 先不加锁跑一次（记下数字）
  4. 再把那三行用 with lock: 包起来，跑第二次

你应该看到：
  不加锁 → 约 20（期望是 80，少了一大半！）
  加锁   → 正好 80

想一想：为什么少掉的那些更新不见了？
"""
import time
import threading

counter = 0
lock = threading.Lock()


def add():
    global counter
    for _ in range(20):
        # TODO 第 3 步：先用这三行跑一遍（不加锁）
        # tmp = counter
        # time.sleep(0.001)
        # counter = tmp + 1
        #
        # TODO 第 4 步：改成下面这样（加锁）再跑一遍
        # with lock:
        #     tmp = counter
        #     time.sleep(0.001)
        #     counter = tmp + 1
        raise NotImplementedError("实现 add()")


def main():
    # TODO: 4 个线程跑 add，start 后全部 join，最后打印 counter
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
