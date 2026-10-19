# -*- coding: utf-8 -*-
"""题 08 · 线程通信：Queue 与 Event

(a) queue.Queue 版
    写线程 put 三个值，再 put(None) 作为结束标记；
    读线程循环 get()，读到 None 就 break。

(b) threading.Event 版
    工作线程一上来就 event.wait()（卡住）；
    主线程 sleep(2) 后 event.set()；
    工作线程被放行后打印「[工作线程] 收到信号，开始干活」。

预期：
  (a) 三个值按顺序被读走，程序正常结束
  (b) 前 2 秒什么都不打印，set() 之后才出现那句话

自测：
  1. 为什么用 Queue 比「共享 list + 加锁」更省心？
  2. Event 和 Condition 各适合什么场景？
  3. put(None) 这种「哨兵值」的作用是什么？
"""
import time
import threading
from queue import Queue


def part_a():
    """Queue 版：写 3 个值 + None 哨兵，读线程读到 None 退出。"""
    # TODO
    raise NotImplementedError("实现 part_a()")


def part_b():
    """Event 版：工作线程 wait，主线程 2 秒后 set。"""
    # TODO
    raise NotImplementedError("实现 part_b()")


def main():
    # TODO: 先跑 (a) 再跑 (b)
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
