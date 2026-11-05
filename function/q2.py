# @Version:   1.0
# @Author:    huangsenyue
import sys
import calendar


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        y = int(input_data[idx])
        m = int(input_data[idx + 1])
        x = input_data[idx + 2]
        idx += 3

        days = calendar.monthrange(y, m)[1]
        count = 0

        for d in range(1, days + 1):
            date_str = f"{y:04d}-{m:02d}-{d:02d}"
            count += date_str.count(x)

        print(count)


if __name__ == "__main__":
    solve()