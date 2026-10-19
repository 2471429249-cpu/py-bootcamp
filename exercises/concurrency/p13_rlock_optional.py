# -*- coding: utf-8 -*-
"""选做 · RLock（章节里只提了一段，可以先跳过）

对应章节：教学 03 →「3、线程同步与互斥锁」（最后一段 RLock）

要做的事：
  1. 写 lock = threading.Lock()
  2. 同一个线程里连续 acquire 两次（用 timeout=1，避免卡死）：
         print("第一次:", lock.acquire(timeout=1))
         print("第二次:", lock.acquire(timeout=1))
  3. 把 lock 换成 threading.RLock()，再跑一次

你应该看到：
  普通 Lock：第一次 True，第二次 False
  RLock    ：两次都是 True

想一想：为什么同一个线程拿同一把普通锁会失败？
"""
import threading


def main():
    # TODO 1: Lock 版实验
    # TODO 2: RLock 版实验
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
