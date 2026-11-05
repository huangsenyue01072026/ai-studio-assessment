# @Version:   1.0
# @Author:    huangsenyue
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    t = int(input_data[1])
    s = input_data[2]

    if '.' not in s:
        print(s)
        return

    int_part, frac_part = s.split('.')
    frac_list = list(frac_part)

    pos = -1
    for i in range(len(frac_list)):
        if frac_list[i] >= '5':
            pos = i
            break

    if pos == -1:
        print(s)
        return

    operations = 0
    while operations < t and pos > 0:
        if frac_list[pos] >= '5':
            frac_list[pos - 1] = str(int(frac_list[pos - 1]) + 1)
            frac_list = frac_list[:pos]
            pos -= 1
            operations += 1
        else:
            break

    if pos == 0 and frac_list[0] >= '5' and operations < t:
        int_part = str(int(int_part) + 1)
        frac_list = []

    if not frac_list:
        print(int_part)
    else:
        print(int_part + '.' + ''.join(frac_list))


if __name__ == '__main__':
    solve()