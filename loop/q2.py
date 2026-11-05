# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)

        num = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(f"{num:>4}", end="")
                num += 1
            print()


if __name__ == "__main__":
    solve()