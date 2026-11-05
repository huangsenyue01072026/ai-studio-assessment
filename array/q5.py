# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))

    if n == 1:
        if a[0] == 0:
            print("UP")
        elif a[0] == 15:
            print("DOWN")
        else:
            print("-1")
    else:
        if a[-1] == 15:
            print("DOWN")
        elif a[-1] == 0:
            print("UP")
        elif a[-1] > a[-2]:
            print("UP")
        else:
            print("DOWN")


if __name__ == "__main__":
    solve()