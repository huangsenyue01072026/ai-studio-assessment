# @Version:   1.0
# @Author:    huangsenyue
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    m = int(input_data[2])

    ans = 0
    for i in range(2, n + 1):
        ans = (ans + m) % i

    ans = (ans + k) % n
    print(ans)

if __name__ == "__main__":
    solve()