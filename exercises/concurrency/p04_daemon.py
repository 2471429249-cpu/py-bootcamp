# -*- coding: utf-8 -*-
"""第 4 题 · daemon：主线程结束了子线程怎么办

对应章节：教学 03 →「6、后台线程」

要做的事：
  1. countdown() 循环 5 次：打印「倒计时 i」，每次 sleep(0.5)
  2. main()：创建线程 → start() → 主线程 sleep(1) → 打印「主线程结束」
  3. 版本 A：原样跑（不设 daemon）
  4. 版本 B：在 start() 之前加 t.daemon = True，再跑

你应该看到：
  A → 主线程结束后程序还要跑一会儿（倒计时打完 5 次）
  B → 主线程结束后程序立刻退出（倒计时只打 2 次左右）
"""
import time
import threading


def countdown():
    # TODO: 循环 5 次，打印「倒计时 i」并 sleep(0.5)
    raise NotImplementedError("实现 countdown()")


def main():
    t = threading.Thread(target=countdown)
    # TODO 版本 A：直接 start()，主线程 sleep(1) 后打印「主线程结束」
    # TODO 版本 B：t.daemon = True（在 start 之前），再跑一遍对比
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
