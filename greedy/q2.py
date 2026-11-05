# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    # 逐行读取输入，处理所有测试用例
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue

        skip = {
            (1, 3): 2, (3, 1): 2,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (1, 7): 4, (7, 1): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 9): 6, (9, 3): 6,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5
        }

        visited = set()
        valid = True

        for i in range(len(s)):
            curr = int(s[i])

            # 规则1：每个数字最多只能使用一次
            if curr in visited:
                valid = False
                break

            # 规则2：检查路径上是否跨越了未访问的中间点
            if i > 0:
                prev = int(s[i - 1])
                if (prev, curr) in skip:
                    mid = skip[(prev, curr)]
                    if mid not in visited:
                        valid = False
                        break

            visited.add(curr)

        if valid:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()