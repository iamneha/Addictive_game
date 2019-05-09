import sys
from collections import defaultdict
sys.stdin = open(sys.argv[1])
inp = list(map(int, input().split()))
rows, cols, num_positions, numbers = inp[0], inp[1], inp[2], inp[3:]


store = defaultdict(list)
for p, c, in zip(numbers[0::2], numbers[1::2]):
    store[c].append(p)


def get_position(num, cols):
    t_row = num // cols
    t_col = num % cols
    if t_col != 0:
        t_row += 1
    else:
        t_col = cols
    return t_row, t_col


def calculate_distance(num1, num2, cols):
    r1, c1 = get_position(num1, cols)
    r2, c2 = get_position(num2, cols)
    return abs(r1-r2) + abs(c1-c2)


result = list()
for colors in sorted(store.keys()):
    _distance = calculate_distance(*store[colors], cols)
    result.append(_distance)

print(' '.join(map(str, result)))
