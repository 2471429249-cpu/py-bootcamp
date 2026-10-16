# -*- coding: utf-8 -*-
"""练习 09：词频统计

练习点：
- 字符串 split() 分词
- 字典统计（手写）与 collections.Counter（标准库）对比
- sorted 按词频排序（key 参数、lambda）
"""

from collections import Counter

# 内置示例文本（简化：按空格分词，不处理标点）
TEXT = (
    "python is great and python is easy "
    "learn python every day because python powers AI "
    "AI and python go together"
)


def count_words_manual(text):
    """手写版：字典统计词频"""
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def main():
    manual = count_words_manual(TEXT)
    print("手写统计：", manual)

    counter = Counter(TEXT.lower().split())
    print("Counter  :", dict(counter))

    # 按词频从高到低排序
    top = counter.most_common(3)
    print("出现最多的 3 个词：", top)


if __name__ == "__main__":
    main()
