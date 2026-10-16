# -*- coding: utf-8 -*-
"""练习 08：列表去重（保持原有顺序）

练习点：
- set 集合（去重、O(1) 查找）
- 手写「见过去重」循环
- 简洁写法：dict.fromkeys（字典键唯一且保持插入顺序）
"""


def dedup_manual(seq):
    """手写版：用 seen 集合记录已出现元素"""
    seen = set()
    result = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def dedup_pythonic(seq):
    """简洁版：dict.fromkeys 保序去重"""
    return list(dict.fromkeys(seq))


def main():
    data = [3, 1, 2, 3, 2, 1, 4, 4, 5, 1]
    print("原始：", data)
    print("手写去重：", dedup_manual(data))
    print("简洁去重：", dedup_pythonic(data))


if __name__ == "__main__":
    main()
