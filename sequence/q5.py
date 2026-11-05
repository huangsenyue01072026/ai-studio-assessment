# @Version:   1.0
# @Author:    huangsenyue
for i in range(1,10):
    tmp = []
    for j in range(1, i+1):
        s = f"{j}*{i}={i*j:2d}"
        tmp.append(s)
    print(' '.join(tmp))