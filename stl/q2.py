# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    A = [int(x) for x in input_data[2:2 + n]]
    B = [int(x) for x in input_data[2 + n:2 + 2 * n]]

    chocolates = [(A[i] - B[i], B[i]) for i in range(n)]
    chocolates.sort(key=lambda x: x[0], reverse=True)

    max_sweetness = 0
    for i in range(n):
        if i < k:
            max_sweetness += (chocolates[i][0] + chocolates[i][1])
        else:
            max_sweetness += chocolates[i][1]

    print(max_sweetness)


if __name__ == '__main__':
    solve()