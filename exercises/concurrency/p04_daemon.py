# -*- coding: utf-8 -*-
"""题 04 · daemon：主线程退出后，子线程会怎样

长任务线程：循环 10 次，每次打印心跳 + sleep(0.5)（约 5 秒）。
主线程 sleep(1) 后打印「[主线程] 结束」。

版本 A：不设 daemon（默认 False）
版本 B：t.daemon = True（必须在 start() 之前设置）

预期：
  A → 主线程结束后程序还要再等约 4 秒（子线程要跑完）
  B → 主线程结束程序立刻退出，心跳只打了两三次

自测：
  1. daemon 在 start() 之后设置会怎样？
  2. 为什么 daemon 线程不适合「必须把文件写完」的任务？
"""
import time
import threading


def heartbeat():
    # TODO: 循环 10 次，打印心跳并 sleep(0.5)
    raise NotImplementedError("实现 heartbeat()")


def main():
    # TODO: 版本 A —— 不设 daemon，跑一次
    # TODO: 版本 B —— t.daemon = True 之后再 start()，再跑一次
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
