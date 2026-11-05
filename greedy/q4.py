# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])

    mapping = {
        "zero": "0",
        "two": "2",
        "four": "4",
        "six": "6",
        "nine": "9",
        "0": "0",
        "2": "2",
        "4": "4",
        "6": "6",
        "9": "9"
    }

    keys = sorted(mapping.keys(), key=len, reverse=True)

    for i in range(1, t + 1):
        s = input_data[i]
        res = []
        j = 0
        n = len(s)

        while j < n:
            matched = False
            for key in keys:
                if s.startswith(key, j):
                    res.append(mapping[key])
                    j += len(key)
                    matched = True
                    break
            if not matched:
                j += 1

        print("".join(res))


if __name__ == '__main__':
    solve()