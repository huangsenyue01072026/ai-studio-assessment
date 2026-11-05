# @Version:   1.0
# @Author:    huangsenyue
a, b = map(int, input().split())
if a < b:
    print("<")
elif a == b:
    print("=")
else:
    print(">")