# @Version:   1.0
# @Author:    huangsenyue
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    for i in range(1, t + 1):
        n = int(input_data[i])
        mid = n // 2
        for r in range(n):
            if r <= mid:
                spaces = mid - r
                stars = 2 * r + 1
            else:
                spaces = r - mid
                stars = 2 * (n - r) - 1
            print(" " * spaces + "*" * stars)

if __name__ == "__main__":
    solve()