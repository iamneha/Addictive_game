import sys
sys.stdin = open(sys.argv[1])
inp = input().split()
rows, cols, num_of_points = int(inp[0]), int(inp[1]), int(inp[2])
skip = 3 + num_of_points * 2
color_numbers = list(map(int, inp[3: skip]))
num_of_paths = int(inp[skip])
start_color_code = int(inp[skip + 1])
starting_position = int(inp[skip + 2])
length = int(inp[skip + 3])
directions = inp[skip+3+1:]
all_positions = {}
path_traversed = []


def get_position(num):
    t_row = num // cols
    t_col = num % cols
    if t_col != 0:
        t_row += 1
    else:
        t_col = cols
    return t_row, t_col


for p, c, in zip(color_numbers[0::2], color_numbers[1::2]):
    all_positions[get_position(p)] = c


def calculate_direction(cur_row, cur_col, direction):
    r, c = cur_row, cur_col
    steps = {
        'N': (r-1, c),
        'E': (r, c+1),
        'S': (r+1, c),
        'W': (r, c-1)
    }
    return steps.get(direction)


def validate(cur_row, cur_col, cur_color):
    """
    Returns:
        -1: invalid
        0: not same color, but allowed to traverse
        1: valid
    """
    if cur_col > cols or cur_row > rows:
        return -1
    if (cur_row, cur_col) in path_traversed:
        return -1
    if (cur_row, cur_col) not in all_positions:
        return 0
    elif all_positions[(cur_row, cur_col)] != cur_color:
        return -1
    return 1


steps = 0
# starting cordinates
r, c = get_position(starting_position)
path_traversed.append((r, c))
color = start_color_code

for _dir in directions:
    r, c = calculate_direction(r, c, _dir)
    status = validate(r, c, color)
    path_traversed.append((r, c))
    steps += 1
    if status == -1:
        break

status = -1 if status == 0 else status

print(status, steps)
