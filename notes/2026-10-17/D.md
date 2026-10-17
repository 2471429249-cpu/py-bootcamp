# Python 学习笔记截图转写（note37 / 38 / 50 / 51 / 52 / 54）

> 转写说明：按截图逐字转写，代码保持原样（含缩进、空格、运算符、标点）；图中的代码框工具条文字（`PYTHON` / `python`、复制、下载、试运行）也一并标注；高亮、警告样式的内容用引用块或 ⚠️ 标出。

## 图 note37

知识点：做「成员判断」时 set 的查找复杂度接近 O(1)、list 是 O(n)，所以代码里有大量 `in` 判断时应先把 list 转成 set。

**5、什么时候该用 set 而不是 list？**

最后这一点很重要。我们做「成员判断」（`x in collection`）的时候：

- 如果 `collection` 是 list，复杂度是 **O(n)**——元素越多越慢
- 如果 `collection` 是 set（或 dict），复杂度接近 **O(1)**——跟元素数量基本无关

所以，如果代码里有大量「这个东西在不在那一堆里」的判断，**把 list 转成 set 性能会大幅提升**：

〔代码块工具条：PYTHON ｜ 复制 ｜ ▶ 试运行〕

```python
names_list = [f'user_{i}' for i in range(100000)]
names_set = set(names_list)

# 这两种结果一样，但是后者快得多
print('user_99999' in names_list)
print('user_99999' in names_set)
```

`set` 的价值不光是去重，更重要的是**快查**。

## 图 note38

知识点：`dict.fromkeys(seq)` 把序列里的每个元素当「键」，没指定「值」时这些键的值默认都是 `None`。

**1. `dict.fromkeys(seq)` 是什么？**

这是字典（dict）的一个内置方法。它的作用是把 `seq` 里的每一个元素拿出来，当作字典的“键（key）”。

因为没有给这些键指定“值（value）”，所以它们的值默认都是 `None`。

## 图 note50

知识点：用一个列表 `a=[3, 1, 2, 3, 2, 1, 4, 4, 5, 1]` 对比三种「去重且保持原顺序」的写法——手动判重（sort1）、set 辅助判重（sort2）、`dict.fromkeys`（sort3）。

> 截图为深色编辑器里的纯代码，没有正文说明文字；`def sort3` 里的 `return list(dict.fromkeys(a))` 这一整行处于选中／当前行高亮状态，且 `(dict.fromkeys(a))` 处带有括号匹配高亮，行首有缩进参考线。

```python
def main():
    a=[3, 1, 2, 3, 2, 1, 4, 4, 5, 1]
    print(sort1(a))
    print(sort2(a))
    print(sort3(a))
def sort1(a):
    b=[]
    for x in a:
        if x not in b:
            b.append(x)
    return b
def sort2(a):
    b=set()
    c=[]
    for x in a:
        if x not in b:
            b.add(x)
            c.append(x)
    return c
def sort3(a):
    return list(dict.fromkeys(a))

if __name__ == '__main__':
    main()
```

## 图 note51

知识点：`sorted()` / `.sort()` 的三个核心参数分别是「排序对象（数据）」、「排序规则（`key=`）」和「排序方向（`reverse=`）」。

> （图中“1 / 2 / 3”是蓝色方块样式的序号标记。）

📝 **Python 排序函数核心笔记（`sorted` / `.sort()`）**

### 一、三个核心参数的作用

在 `sorted(数据, key=规则, reverse=方向)` 中：

**1 第一个参数：排序的对象（数据）**

- 作用：你要排序的目标。
- 要求：必须是可迭代对象（列表、元组、字典的 `items()` 等）。
- 注意：它必须放在第一个位置。

**2 第二个参数：排序的规则（`key=`）**

- 基础理解：你选择排序的主要参考索引。
  - 例如按工资排：`key=lambda x: x[1]`
- 进阶补充：`key` 其实非常灵活，它不局限于索引：
  1. 可以是计算公式：比如按绝对值排 `key=abs`，按字符串长度排 `key=len`。
  2. 可以是多维标准（元组）：如果“主要参考”打平了，可以指定“次要参考”。写法是返回一个元组，比如 `key=lambda x: (x[1], x[2])`（先按工资排，工资一样按年龄排）。

**3 第三个参数：排序的方向（`reverse=`）**

- 基础理解：固定用于要求正序或倒序，没有其他作用。
  - `reverse=False`：正序（从小到大），默认值，可省略。
  - `reverse=True`：倒序（从大到小）。
- 进阶补充：它的位置不固定，写在 `key` 前面或后面都可以（但习惯上写在最后）。

## 图 note52

知识点：`.split()` 会把字符串变成列表，而列表没有 `.replace()` 方法，所以必须“先清洗、后切分”。

📝 **文本清洗与分词笔记**

⚠️ **核心铁律**

`.split()` 会把字符串变成列表。列表没有 `.replace()` 方法！

❌ **错误写法**

〔代码块工具条：python ｜ 复制 ｜ 下载〕

```python
# split() 放在了 replace() 前面，导致后面报错 'list' object has no attribute 'replace'
n = input().lower().split().replace(",", " ")
```

✅ **正确写法（口诀：先清洗，后切分）**

〔代码块工具条：python ｜ 复制 ｜ 下载〕

```python
# 顺序：输入 -> 转小写 -> 替换标点 -> 最后切分
n = input().lower().replace(",", " ").replace(".", " ").split()
```

## 图 note54

知识点：`sorted` 的完整结构是 `sorted(数据, key=规则, reverse=真假)`，第一个位置必须给数据，后两个是带默认值的可选参数。

**1. `sorted` 本身长什么样？**

当你写 `sorted(数据)` 的时候，其实你只用了它最基础的功能。

`sorted` 这个函数在设计的时候，官方考虑到：“很多时候，用户想排序，但他们想比对的规则不一样。有的想按长度，有的想按大小写，有的想按字典的 value，我总不能写几百个不同的排序函数吧？”

所以，官方把 `sorted` 的完整结构设计成了这样：

〔代码块工具条：python ｜ 复制 ｜ 下载〕

```python
sorted(数据, key=规则, reverse=真假)
```

- 第一个位置（数据）：必须给，不给没东西排。
- 后面几个（`key`、`reverse`）：是“可选参数”（有默认值）。你不加，它就用默认的；你加了，它就按你说的办。

**关键点：** `key` 后面的那个值，官方要求必须是一个“函数”（或者任何能被调用的东西）。
