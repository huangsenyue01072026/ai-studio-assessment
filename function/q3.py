# @Version:   1.0
# @Author:    huangsenyue
import sys
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = input_data[0]
    rev_t = t[::-1]
    num = int(rev_t)

    if is_prime(num):
        print("prime")
    else:
        print("noprime")


if __name__ == "__main__":
    solve()