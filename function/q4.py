# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x = int(input_data[0])
    y = int(input_data[1])

    start = min(x, y)
    end = max(x, y)

    count = 0
    for i in range(start, end + 1):
        s = sum(int(digit) for digit in str(i))
        if s % 5 == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()