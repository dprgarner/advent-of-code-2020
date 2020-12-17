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


def print_cells(cells):
    z_layers = []
    x_layers = []
    y_layers = []
    for (x, y, z) in cells:
        x_layers.append(x)
        y_layers.append(y)
        z_layers.append(z)

    for z in range(min(z_layers), max(z_layers) + 1):
        print('z={}:'.format(z))
        rows = []
        for x in range(min(x_layers), max(x_layers) + 1):
            row = []
            for y in range(min(y_layers), max(y_layers) + 1):
                row.append(
                    '#'
                    if (x, y, z) in cells
                    else '.'
                )
            rows.append(row)
        print('\n'.join(
            ''.join(c for c in row)
            for row in rows
        ))
        print('\n')


neighbours = [
    (x, y, z)
    for x in (-1, 0, 1)
    for y in (-1, 0, 1)
    for z in (-1, 0, 1)
    if x != 0 or y != 0 or z != 0
]


def iterate(cells):
    """
    This iteration approach doesn't keep track of where the original coordinates
    or origin was during iteration, because the only thing we care about is the
    final count of cells.
    """

    z_layers = []
    x_layers = []
    y_layers = []
    for (x, y, z) in cells:
        x_layers.append(x)
        y_layers.append(y)
        z_layers.append(z)

    new_cells = set()
    for z in range(min(z_layers) - 1, max(z_layers) + 2):
        for y in range(min(y_layers) - 1, max(y_layers) + 2):
            for x in range(min(x_layers) - 1, max(x_layers) + 2):
                count_neighbours = 0
                for (i, j, k) in neighbours:
                    if (x+i, y+j, z+k) in cells:
                        count_neighbours += 1
                if (
                    count_neighbours == 3 or
                    (x, y, z) in cells and count_neighbours in (2, 3)
                ):
                    new_cells.add((x, y, z))
    return new_cells


def main():
    cells = {
        (x, y, 0)
        for (x, row) in enumerate(parse_input())
        for (y, c) in enumerate(row)
        if c
    }
    for _ in range(6):
        cells = iterate(cells)
    print('Total active cells:', len(cells))


main()
