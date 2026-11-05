# @Version:   1.0
# @Author:    huangsenyue
while True:
    try:
        n = int(input())
        for i in range(1, n + 2):
            print(" " * (2*(n - i + 1)) + "*" * i)
        for i in range(n, 0, -1):
            print(" " * (2*(n - i + 1)) + "*" * i)
    except EOFError:
        break