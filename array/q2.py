# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    x = int(input_data[1])

    count = 0
    x_str = str(x)

    for i in range(1, n + 1):
        count += str(i).count(x_str)

    print(count)


if __name__ == "__main__":
    solve()