# -*- coding: utf-8 -*-
"""题 05 · 竞态条件与锁（本章最重要的一题）

四小步，每步都要把「期望 / 实际」记下来对比：

  (a) 8 线程 × 20 万次 counter += 1
      → 实测结果 1,600,000，完全正确（撞不上）

  (b) 把 +1 拆成读-改-写，并在中间主动让出：
          tmp = counter
          time.sleep(0)
          counter = tmp + 1
      8 线程 × 500 次（期望 4000）
      → 实测只剩约 700~800

  (c) 给 (b) 的临界区加 threading.Lock → 恢复 4000

  (d) 用 with lock: 重写 (c) → 同样 4000

重点体会：(a) 对而 (b) 错，证明「有 GIL 也不等于线程安全」。

自测：
  1. (a) 和 (b) 的差别到底在哪一步？
  2. 「GIL 保证了线程安全」这句错在哪？
  3. 为什么加了 sleep(0) 就必错？
  4. 加锁之后为什么变慢了？值得吗？
"""
import time
import threading

counter = 0
lock = threading.Lock()


def add_plain(iters):
    """(a) 普通 += ：全局 counter 自增 iters 次。"""
    global counter
    # TODO
    raise NotImplementedError("实现 add_plain()")


def add_rmw(iters):
    """(b) 读-改-写 + 主动让出。"""
    global counter
    # TODO: tmp = counter / time.sleep(0) / counter = tmp + 1
    raise NotImplementedError("实现 add_rmw()")


def add_locked(iters):
    """(c) 加锁的读-改-写。"""
    global counter
    # TODO: 用 lock 把三步包起来
    raise NotImplementedError("实现 add_locked()")


def add_with_statement(iters):
    """(d) 用 with lock: 的写法。"""
    global counter
    # TODO: with lock:
    raise NotImplementedError("实现 add_with_statement()")


def run_case(label, target, n_threads, iters):
    """通用跑法：重置 counter → 开线程 → join → 打印「期望/实际」。"""
    # TODO
    raise NotImplementedError("实现 run_case()")


def main():
    # TODO: 依次跑 (a)(b)(c)(d)
    raise NotImplementedError("实现 main()")


if __name__ == "__main__":
    main()
