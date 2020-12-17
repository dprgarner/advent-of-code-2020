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


neighbours = [
    (x, y, z, w)
    for x in (-1, 0, 1)
    for y in (-1, 0, 1)
    for z in (-1, 0, 1)
    for w in (-1, 0, 1)
    if x != 0 or y != 0 or z != 0 or w != 0
]


def iterate(cells):
    """
    This iteration approach doesn't keep track of where the original coordinates
    or origin was during iteration, because the only thing we care about is the
    final count of cells.
    """

    x_layers = []
    y_layers = []
    z_layers = []
    w_layers = []
    for (x, y, z, w) in cells:
        x_layers.append(x)
        y_layers.append(y)
        z_layers.append(z)
        w_layers.append(w)

    new_cells = set()
    for w in range(min(w_layers) - 1, max(w_layers) + 2):
        for z in range(min(z_layers) - 1, max(z_layers) + 2):
            for y in range(min(y_layers) - 1, max(y_layers) + 2):
                for x in range(min(x_layers) - 1, max(x_layers) + 2):
                    count_neighbours = 0
                    for (i, j, k, l) in neighbours:
                        if (x+i, y+j, z+k, w+l) in cells:
                            count_neighbours += 1
                    if (
                        count_neighbours == 3 or
                        (x, y, z, w) in cells and count_neighbours in (2, 3)
                    ):
                        new_cells.add((x, y, z, w))
    return new_cells


def main():
    cells = {
        (x, y, 0, 0)
        for (x, row) in enumerate(parse_input())
        for (y, c) in enumerate(row)
        if c
    }
    for _ in range(6):
        cells = iterate(cells)
    print('Total active cells:', len(cells))


main()
