# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = list(map(int, input_data[idx:idx + n]))
        idx += n

        max_val = max(arr)
        min_val = min(arr)
        extreme_diff = max_val - min_val

        mean = sum(arr) / n

        variance = sum((x - mean) ** 2 for x in arr) / n

        print(f"{extreme_diff} {variance:.3f}")


if __name__ == "__main__":
    solve()