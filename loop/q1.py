# @Version:   1.0
# @Author:    huangsenyue
import sys

def solve():
    # 处理多组输入
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

        for i in range(1, n):
            spaces = " " * i
            stars = "*" * (2 * (n - i) - 1)
            print(spaces + stars)

if __name__ == "__main__":
    solve()