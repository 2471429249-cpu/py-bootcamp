# py-bootcamp · Python 学习起步仓库

> 这是你「AI 专业 Python 从零到精通」路线的 **P0 交付物**。
> 目标：搭好环境、跑通 10 个迷你练习、养成 Git 提交与记录学习日志的习惯。

## 一、你的环境现状（已检查确认）

| 项目 | 位置 / 版本 | 说明 |
|---|---|---|
| Anaconda | `C:\python11111` · Python **3.14.6** · conda 26.5.3 | ✅ 已装好，自带 Jupyter |
| Python（另一套） | `C:\Users\边角\AppData\Local\Programs\Python\Python313` · 3.13.7 | 当前 `python` 命令指向它 |
| PyCharm | 2025.2 | ✅ 已装好 |
| Git | ❌ 未安装 | 见下面「安装 Git」 |
| Jupyter | `C:\python11111\Scripts\jupyter.exe` | Anaconda 自带 |

> ⚠️ **你有两套 Python**：PATH 里的 `python` 是 3.13.7，Anaconda 是 3.14.6。
> 这两套都能跑本仓库的练习（只用标准库），但以后做数据科学/机器学习时，
> **请统一用 Anaconda 那套**，避免「装了库却找不到」的经典问题。

## 二、怎么运行练习

**方式 A：命令行（推荐先用这个）**

```powershell
# 用 Anaconda 的 Python 运行（推荐）
C:\python11111\python.exe exercises\01_variable_swap.py

# 或用 PATH 上的 Python 3.13
python exercises\01_variable_swap.py
```

**方式 B：PyCharm**

1. 打开本文件夹（File → Open）。
2. 右下角解释器选择 Anaconda：`File → Settings → Project → Python Interpreter → Add Interpreter → Conda → Existing`，指向 `C:\python11111\python.exe`。
3. 右键某个 `exercises\*.py` → Run。

**方式 C：Jupyter（写实验笔记）**

```powershell
C:\python11111\Scripts\jupyter.exe notebook
```

## 三、练习清单（10 个，按难度递进）

| 文件 | 练习内容 | 练到的知识点 |
|---|---|---|
| `01_variable_swap.py` | 变量交换 | 变量、多重赋值 |
| `02_calculator.py` | 简易计算器 | 函数、input、类型转换、分支 |
| `03_temperature.py` | 摄氏/华氏换算 | 函数、公式、格式化 |
| `04_guess_number.py` | 猜数字游戏 | random、while、比较、计数 |
| `05_multiplication_table.py` | 九九乘法表 | 嵌套 for、range、对齐 |
| `06_fibonacci.py` | 斐波那契数列 | 列表、循环、生成器 |
| `07_reverse_string.py` | 字符串反转 | 切片、reversed、join |
| `08_list_dedup.py` | 列表去重 | set、dict.fromkeys |
| `09_word_frequency.py` | 词频统计 | 字典、Counter、排序 |
| `10_file_io.py` | 读写文本文件 | with open、pathlib |

每个练习都是**可直接运行的独立脚本**，顶部注释写了「练习点」。

## 四、学习日志

每天花 2 分钟在 [`daily-log.md`](daily-log.md) 里写一行：今天学了什么、遇到什么问题、怎么解决的。
这份日志是你求职时「持续学习」的直接证据。

## 五、安装 Git 并推上 GitHub

Git 目前未安装。装好后执行：

```powershell
# 1) 安装 Git：去 https://git-scm.com/download/win 下载安装（一路默认即可）
# 2) 设置身份（首次）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 3) 初始化本仓库并提交
cd C:\Users\边角\Desktop\py-bootcamp
git init
git add .
git commit -m "P0: 环境搭建 + 10 个入门练习"

# 4) 在 GitHub 上新建空仓库 py-bootcamp，然后：
git remote add origin https://github.com/<你的用户名>/py-bootcamp.git
git branch -M main
git push -u origin main
```

## 六、下一步（P1）

环境跑通后，进入路线 P1：Python 核心语法 + 高级特性，目标产出 `neurocards`（终端间隔重复背题系统）。
