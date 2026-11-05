# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]

    a.sort()

    for i in range(n - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            ans = [a[i], a[i + 1], a[i + 2]]
            if i + 3 < n and ans[0] + ans[1] > a[i + 3]:
                ans[2] = a[i + 3]

            print(f"{ans[0]} {ans[1]} {ans[2]}")
            return

    print("No solution")


if __name__ == '__main__':
    solve()