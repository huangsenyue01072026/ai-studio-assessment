# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    counts = [int(x) for x in input_data[:10]]

    pairs = []
    middle = ""

    for i in range(10):
        pairs.extend([str(i)] * (counts[i] // 2))
        if counts[i] % 2 == 1 and middle == "":
            middle = str(i)

    if not pairs:
        for i in range(1, 10):
            if counts[i] > 0:
                print(i)
                return
        if counts[0] > 0:
            print("0")
            return
        print("-1")
        return

    pairs.sort()

    if pairs[0] == '0':
        for i in range(1, len(pairs)):
            if pairs[i] != '0':
                pairs[0], pairs[i] = pairs[i], pairs[0]
                break

    left = "".join(pairs)
    right = left[::-1]

    print(left + middle + right)


if __name__ == '__main__':
    solve()