# -*- coding: utf-8 -*-
"""第 2 题 · 继承 Thread 类来创建线程

对应章节：教学 03 →「1、线程的创建」

要做的事：
  1. MyThread 继承 threading.Thread，重写 run()
  2. run() 里循环 3 次：打印 self.name + 序号，然后 sleep(0.5)
  3. main() 里创建 2 个 MyThread，都 start()，再都 join()

你应该看到：Thread-1 / Thread-2 的输出交错出现，顺序每次都不太一样。
"""
import time
import threading


class MyThread(threading.Thread):
    def run(self):
        # TODO: 循环 3 次，打印 self.name 和 i，每次 sleep(0.5)
        raise NotImplementedError("实现 MyThread.run()")


def main():
    # TODO: 创建 2 个 MyThread → start() → join()
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
