# @Version:   1.0
# @Author:    huangsenyue
import sys
import functools


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    nums = input_data[1:n + 1]

    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    nums.sort(key=functools.cmp_to_key(compare))

    print("".join(nums))


if __name__ == '__main__':
    solve()