# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    s = sys.stdin.read()
    res = []
    n = len(s)
    i = 0
    in_comment = False
    in_string = False
    comment_start = -1

    while i < n:
        if in_comment:
            if i + 1 < n and s[i] == '*' and s[i + 1] == '/':
                in_comment = False
                i += 2
            else:
                i += 1
        elif in_string:
            res.append(s[i])
            if s[i] == '\\' and i + 1 < n:
                res.append(s[i + 1])
                i += 2
            elif s[i] == '"':
                in_string = False
                i += 1
            else:
                i += 1
        else:
            if i + 1 < n and s[i] == '/' and s[i + 1] == '*':
                in_comment = True
                comment_start = i
                i += 2
            elif s[i] == '"':
                in_string = True
                res.append(s[i])
                i += 1
            else:
                res.append(s[i])
                i += 1
    if in_comment:
        res.append(s[comment_start:])

    sys.stdout.write(''.join(res))


if __name__ == '__main__':
    solve()