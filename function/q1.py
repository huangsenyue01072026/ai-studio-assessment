# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L = int(input_data[0])
    R = int(input_data[1])

    count = 0
    for i in range(L, R + 1):
        count += str(i).count('2')

    print(count)


if __name__ == "__main__":
    solve()