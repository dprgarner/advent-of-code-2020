MAX_NEIGHBOURS, CHECK_IN_LINE = (4, False)
# MAX_NEIGHBOURS, CHECK_IN_LINE  = (5, True)


def parse_input():
    grid = []
    try:
        while True:
            row = input()
            grid.append([c for c in row])
    except EOFError:
        pass
    return grid


def find_adjacent_neighbours(grid, i, j):
    height = len(grid)
    width = len(grid[0])
    directions = [
        (k, l)
        for k in [-1, 0, 1]
        for l in [-1, 0, 1]
        if k != 0
        or l != 0
    ]
    neighbours = [(k+i, l+j) for (k, l) in directions]
    seat_neighbours = [
        (k, l)
        for (k, l) in neighbours
        if k >= 0
        and k < height
        and l >= 0
        and l < width
        and grid[k][l] != '.'
    ]
    return seat_neighbours


def find_line_neighbours(grid, i, j):
    height = len(grid)
    width = len(grid[0])
    directions = [
        (k, l)
        for k in [-1, 0, 1]
        for l in [-1, 0, 1]
        if k != 0
        or l != 0
    ]
    seat_neighbours = []
    for (k, l) in directions:
        m, n = i + k, j + l
        while (
            m >= 0
            and m < height
            and n >= 0
            and n < width
        ):
            if grid[m][n] != '.':
                seat_neighbours.append((m, n))
                break
            m += k
            n += l
    return seat_neighbours


def build_neighbours(grid):
    seat_neighbours = []
    for row in grid:
        seat_neighbours.append([
            None for _ in row
        ])

    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '.':
                continue
            if CHECK_IN_LINE:
                seat_neighbours[i][j] = find_line_neighbours(grid, i, j)
            else:
                seat_neighbours[i][j] = find_adjacent_neighbours(grid, i, j)

    return seat_neighbours


def count_neighbours(grid, neighbours):
    full_seats = len([
        (k, l)
        for k, l in neighbours
        if grid[k][l] == '#'
    ])
    return full_seats


def iterate(grid, neighbours):
    new_grid = [[c for c in row] for row in grid]
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '.':
                continue
            full_neighbours = count_neighbours(grid, neighbours[i][j])
            if char == 'L' and full_neighbours == 0:
                new_grid[i][j] = '#'
            if char == '#' and full_neighbours >= MAX_NEIGHBOURS:
                new_grid[i][j] = 'L'
    return new_grid


def print_grid(grid):
    print('\n'.join(''.join(c for c in row) for row in grid))


def recursive_iterate(grid):
    neighbours = build_neighbours(grid)
    new_grid = iterate(grid, neighbours)
    while grid != new_grid:
        grid, new_grid = new_grid, iterate(new_grid, neighbours)
    return grid


def count_full_seats(grid):
    full_seats = 0
    for row in grid:
        for c in row:
            if c == '#':
                full_seats += 1
    return full_seats


grid = parse_input()
stable_grid = recursive_iterate(grid)
print_grid(stable_grid)
print('Full seats:', count_full_seats(stable_grid))
