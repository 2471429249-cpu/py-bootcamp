# -*- coding: utf-8 -*-
"""题 06 · RLock：同一个线程能重复拿同一把锁吗

写一个类：add() 先获取锁，然后调用同类里「也需要获取同一把锁」的 _write()。
版本 A 用 threading.Lock()  → 第二次获取会卡住
版本 B 用 threading.RLock() → 正常通过

⚠️ 安全做法（很重要）：
   把 add() 放到一个【子线程】里执行，主线程 t.join(timeout=2)，
   然后用 t.is_alive() 判断它是不是卡住了。
   千万不要在主线程直接调用 add()，否则你的程序会真的卡死。

预期：A 的 is_alive() 为 True（卡住）；B 正常结束。

自测：
  1. 什么场景真的需要 RLock？
  2. 为什么普通 Lock 不可重入？
"""
import threading


class LockedWriter:
    """版本 A：普通 Lock。"""

    def __init__(self):
        self.lock = threading.Lock()

    def add(self, value):
        # TODO: 获取锁 → 调 self._write(value) → 释放锁
        raise NotImplementedError("实现 LockedWriter.add()")

    def _write(self, value):
        # TODO: 这里也要获取同一把锁（A 版本会在这里卡死）
        raise NotImplementedError("实现 LockedWriter._write()")


class RLockedWriter(LockedWriter):
    """版本 B：只把锁换成 RLock，逻辑不变。"""

    def __init__(self):
        self.lock = threading.RLock()


def try_case(label, writer):
    """在子线程里调用 writer.add()，2 秒后看它是否还活着。"""
    # TODO: 起线程 → join(timeout=2) → 打印 is_alive()
    raise NotImplementedError("实现 try_case()")


def main():
    # TODO: try_case("Lock", LockedWriter()) 和 try_case("RLock", RLockedWriter())
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
