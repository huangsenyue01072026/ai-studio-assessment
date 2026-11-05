# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L = int(input_data[0])
    M = int(input_data[1])

    trees = [True] * (L + 1)

    idx = 2
    for _ in range(M):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        for i in range(l, r + 1):
            trees[i] = False

    print(sum(trees))


if __name__ == "__main__":
    solve()