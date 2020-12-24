"""
Represent:
. . . . . . .
 . . X X . . .
. . X . X . .
 . . X X . . .
. . . . . . .

in a grid as:
. . . . . . .
  . . . X X . .
    . . X . X . .
      . . X X . . .
        . . . . . . .
"""


def parse_input():
    commands = []
    try:
        while True:
            line_str = input()
            line = []
            while line_str:
                chars = (
                    2
                    if line_str.startswith('s') or line_str.startswith('n')
                    else 1
                )
                line.append(line_str[:chars])
                line_str = line_str[chars:]
            commands.append(line)
    except EOFError:
        pass
    return commands


DIRECTION = {
    'w': (-1, 0),
    'nw': (-1, 1),
    'ne': (0, 1),
    'e': (1, 0),
    'se': (1, -1),
    'sw': (0, -1),
}


def get_adjacent(tile, direction):
    x, y = tile
    dx, dy = DIRECTION[direction]
    return (x + dx, y + dy)


def get_tile(command):
    x, y = 0, 0
    for direction in command:
        x, y = get_adjacent((x, y), direction)
    return x, y


def get_initial_tiles(commands):
    flipped_tiles = set()
    for command in commands:
        tile = get_tile(command)
        if tile in flipped_tiles:
            flipped_tiles.remove(tile)
        else:
            flipped_tiles.add(tile)
    return flipped_tiles


def iterate(tiles):
    counts = {}
    for tile in tiles:
        for direction in DIRECTION:
            candidate = get_adjacent(tile, direction)
            if candidate not in counts:
                counts[candidate] = 0
            counts[candidate] = counts[candidate] + 1

    new_tiles = set()
    for tile, count in counts.items():
        if count == 2 or count == 1 and tile in tiles:
            new_tiles.add(tile)

    return new_tiles


def main():
    commands = parse_input()
    tiles = get_initial_tiles(commands)
    print('Number of black tiles:', len(tiles))
    for _ in range(100):
        tiles = iterate(tiles)
    print('Number of black tiles:', len(tiles))


main()
