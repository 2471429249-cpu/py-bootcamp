# -*- coding: utf-8 -*-
"""练习 10：读写文本文件

练习点：
- with open(...) 上下文管理器（自动关闭文件）
- pathlib.Path 面向对象的路径操作
- 写入、读取、追加（append）
"""

from pathlib import Path


def main():
    # 输出文件放在本脚本同目录，避免写到哪里都不清楚
    p = Path(__file__).parent / "sample_output.txt"

    # 1) 写入（覆盖写）
    p.write_text("第一行\n第二行\n", encoding="utf-8")
    print("已写入文件：", p)

    # 2) 读取
    content = p.read_text(encoding="utf-8")
    print("读取到的内容：")
    print(content, end="")

    # 3) 追加一行
    with p.open("a", encoding="utf-8") as f:
        f.write("追加的第三行\n")

    lines = p.read_text(encoding="utf-8").splitlines()
    print(f"最终共 {len(lines)} 行")


if __name__ == "__main__":
    main()
