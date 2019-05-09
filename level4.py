import sys
sys.stdin = open(sys.argv[1])
inp = input().split()
rows, cols, num_of_points = int(inp[0]), int(inp[1]), int(inp[2])
skip = 3 + num_of_points * 2
color_numbers = list(map(int, inp[3: skip]))
num_of_paths = int(inp[skip])
start_color_code = list()
starting_position = list()
length = list()
directions = list()
all_positions = {}
path_traversed = []

for _ in range(num_of_paths):
    start_color_code.append(int(inp[skip+1]))
    starting_position.append(int(inp[skip + 2]))
    length.append(int(inp[skip + 3]))
    new_skip = skip + 3 + length[-1]
    directions.append(inp[skip+4:new_skip+1])
    skip = new_skip


def get_position(num):
    t_row = num // cols
    t_col = num % cols
    if t_col != 0:
        t_row += 1
    else:
        t_col = cols
    return t_row, t_col


def calculate_direction(cur_row, cur_col, direction):
    r, c = cur_row, cur_col
    return {
        'N': (r-1, c),
        'E': (r, c+1),
        'S': (r+1, c),
        'W': (r, c-1)
    }.get(direction)


def validate(cur_row, cur_col, cur_color, path_traversed):
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


def draw():
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if (r, c) in all_positions or (r, c) in path_traversed:
                print('#', end='')
            else:
                print(' ', end='')
        print()


for p, c, in zip(color_numbers[0::2], color_numbers[1::2]):
    all_positions[get_position(p)] = c


for start_color_code, starting_position, length, directions in zip(start_color_code, starting_position, length, directions):
    local_path_traversed = list()

    steps = 0
    r, c = get_position(starting_position)
    local_path_traversed.append((r, c))
    color = start_color_code

    for _dir in directions:
        r, c = calculate_direction(r, c, _dir)
        status = validate(r, c, color, path_traversed + local_path_traversed)
        local_path_traversed.append((r, c))
        steps += 1
        if status == -1:
            break

    status = -1 if status == 0 else status
    if status == 1:
        path_traversed.extend(local_path_traversed)
draw()
