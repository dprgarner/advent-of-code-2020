def parse_input():
    grid = []
    try:
        while True:
            grid.append([
                c == '#'
                for c in input()
            ])
    except EOFError:
        pass
    return grid


def count_trees_in_line(grid, right, down):
    height = len(grid)
    width = len(grid[0])
    trees = 0

    i = 0
    j = 0
    while True:
        i += down
        j += right
        j = j % width
        if i >= height:
            break
        if grid[i][j]:
            trees += 1
    return trees


def check_multiple_slopes(grid, slopes):
    return [
        count_trees_in_line(grid, right, down)
        for right, down in slopes
    ]


def product(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return prod


grid = parse_input()
print('Trees in line 3,1:', count_trees_in_line(grid, 3, 1))

tree_counts = check_multiple_slopes(grid, [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
])
print('Trees in multiple lines:', tree_counts)
print('Product:', product(tree_counts))
