# @Version:   1.0
# @Author:    huangsenyue
res = []
for a in range(1, 100):
    for b in range(a + 1, 10000):
        c = a * b
        s = str(a) + str(b) + str(c)
        if len(s) != 9:
            continue
        if set(s) == {'1','2','3','4','5','6','7','8','9'}:
            res.append((c, a, b))

res.sort(key=lambda x: (x[0], x[1]))
for c, a, b in res:
    print(f"{c} = {a} x {b}")