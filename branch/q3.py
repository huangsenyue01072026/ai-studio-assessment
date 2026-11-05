# @Version:   1.0
# @Author:    huangsenyue
line = input().strip()
lst = line.split()
x = int(lst[0])
y = int(lst[1])
if x == y:
    print("Tacit!")
else:
    print("No Tacit!")