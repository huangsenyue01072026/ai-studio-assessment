# @Version:   1.0
# @Author:    huangsenyue
import itertools

for p in itertools.permutations(range(1, 9)):
    print(*p, sep=" ")