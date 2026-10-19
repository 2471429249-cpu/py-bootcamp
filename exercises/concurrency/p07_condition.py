# -*- coding: utf-8 -*-
"""题 07 · Condition：生产者消费者（基础版）

用 threading.Condition + 一个 list（容量 3）实现：
  - 生产者：生产 10 个产品（编号 1~10），缓冲区满了就 wait()
  - 消费者：消费 10 个，缓冲区空了就 wait()
  - 判断条件必须用 while（不是 if），操作后 notify()

预期：程序正常结束（不死锁），最终「生产 10 个 = 消费 10 个」。

关键提示：
    with cond:
        while len(buffer) >= 3:     # 必须 while（要防虚假唤醒）
            cond.wait()
        buffer.append(item)
        cond.notify()

自测：
  1. 为什么条件判断要用 while 而不是 if？
  2. notify() 和 notify_all() 的区别？
  3. wait() 会自动释放锁吗？
"""
import threading
import time

CAPACITY = 3
buffer = []
cond = threading.Condition()


def producer():
    # TODO: 生产 1..10，满了就 while cond.wait()
    raise NotImplementedError("实现 producer()")


def consumer():
    # TODO: 消费 10 个，空了就 while cond.wait()
    raise NotImplementedError("实现 consumer()")


def main():
    # TODO: 起生产/消费两个线程，start + join
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
