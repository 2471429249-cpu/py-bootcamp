# -*- coding: utf-8 -*-
"""第 6 题 · Condition：等待和通知

对应章节：教学 03 →「4、Condition 条件变量」

要做的事：
  1. waiter()：with cond 里 while not ready: 打印「等待中...」+ cond.wait()
               被唤醒后打印「收到通知，开始干活」
  2. notifier()：sleep(2) → with cond 里把 ready 设为 True 并 cond.notify()
  3. main()：先 start waiter，再 start notifier，两个都 join

你应该看到：先「等待中...」，停 2 秒，然后「收到通知，开始干活」。

注意：ready 是全局变量，在函数里改要写 global ready。
"""
import time
import threading

cond = threading.Condition()
ready = False


def waiter():
    global ready
    # TODO: with cond: while not ready: print + wait()；唤醒后打印
    raise NotImplementedError("实现 waiter()")


def notifier():
    global ready
    # TODO: sleep(2) → with cond: ready = True; cond.notify()
    raise NotImplementedError("实现 notifier()")


def main():
    # TODO: 先 start waiter，再 start notifier，两个都 join
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
