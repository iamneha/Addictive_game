import sys
sys.stdin = open('level1-0.in')
inp = list(map(int, input().split()))
rows, cols, num_positions, numbers = inp[0], inp[1], inp[2], inp[3:]


result = []

for num in numbers:
    t_row = num // cols
    t_col = num % cols
    if t_col != 0:
        t_row += 1
    else:
        t_col = cols
    result += [t_row, t_col]

print(' '.join(map(str, result)))
