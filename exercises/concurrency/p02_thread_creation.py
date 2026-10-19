# -*- coding: utf-8 -*-
"""题 02 · 创建线程的两种方式

方式 A：继承 threading.Thread，重写 run()
方式 B：Thread(target=函数, args=(...))
两种方式都创建 3 个线程，每个线程打印 3 次「线程名 + 序号」。
预期：输出交错出现，每次运行顺序都不同（这就是并发）。

自测：
  1. 为什么继承时要重写 run() 而不是 start()？
  2. 直接调 t.run() 而不调 t.start() 会发生什么？（一定要试一次）
"""
import threading


class MyThread(threading.Thread):
    """方式 A：继承式。"""

    def run(self):
        # TODO: 打印 3 次 self.name + 序号
        raise NotImplementedError("实现 MyThread.run()")


def worker():
    """方式 B：函数式。"""
    # TODO: 打印 3 次 threading.current_thread().name + 序号
    raise NotImplementedError("实现 worker()")


def main():
    # TODO: 用两种方式各创建 3 个线程，start() 后全部 join()
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
