# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    s = sys.stdin.read().strip()
    if not s:
        return

    if len(s) % 2 != 0:
        print("Bad")
        return

    stack = []
    for char in s:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if stack and stack[-1] == 'a':
                stack.pop()
            else:
                print("Bad")
                return
        else:
            print("Bad")
            return

    if not stack:
        print("Good")
    else:
        print("Bad")


if __name__ == '__main__':
    solve()