# @Version:   1.0
# @Author:    huangsenyue
import sys
import string

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    target = line[0]
    n = string.ascii_uppercase.index(target) + 1
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        s = ""
        for j in range(i):
            s += string.ascii_uppercase[j]
        for j in range(i - 2, -1, -1):
            s += string.ascii_uppercase[j]
        print(spaces + s)