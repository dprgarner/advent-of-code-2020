import re


def parse_tile():
    id_ = int(input().replace('Tile ', '').replace(':', ''))
    line = input()
    grid = []
    try:
        while line:
            grid.append(line)
            line = input()
    except EOFError:
        pass
    return id_, grid


def parse_input():
    tiles = {}
    tiles_remain = True
    while tiles_remain:
        try:
            id_, tile = parse_tile()
        except EOFError:
            tiles_remain = False
        tiles[id_] = tile
    return tiles


def build_borders(tiles):
    borders = {}
    for id_, tile in tiles.items():
        border_list = [
            tile[0],
            ''.join(row[-1] for row in tile),
            tile[-1],
            ''.join(row[0] for row in tile),
        ]
        borders[id_] = border_list + [
            ''.join(reversed(border))
            for border in border_list
        ]
    return borders


def iterate_pairs(ids):
    ids = list(ids)
    for index, id1 in enumerate(ids):
        for id2 in ids[index + 1:]:
            yield (id1, id2)


def find_adjacencies(borders):
    adjacencies = {}
    for (id1, id2) in iterate_pairs(borders.keys()):
        if len(set(borders[id1]).intersection(set(borders[id2]))):
            if id1 not in adjacencies:
                adjacencies[id1] = set()
            adjacencies[id1].add(id2)
            if id2 not in adjacencies:
                adjacencies[id2] = set()
            adjacencies[id2].add(id1)
    return adjacencies


def arrange_ids(adjacencies):
    adjacencies = {k: v.copy() for k, v in adjacencies.items()}

    current_id = next(k for k, v in adjacencies.items() if len(v) == 2)
    start_row = [current_id]
    visited = set([current_id])
    while len(adjacencies[current_id]) != 2 or len(start_row) == 1:
        current_id = sorted(
            adjacencies[current_id].difference(visited),
            key=lambda v: len(adjacencies[v])
        )[0]
        start_row.append(current_id)
        visited.add(current_id)

    grid = [start_row]
    visited = set(start_row)
    try:
        while True:
            row = []
            for i in grid[-1]:
                next_id = adjacencies[i].difference(visited).pop()
                if not next_id:
                    return grid
                row.append(next_id)
            grid.append(row)
            visited.update(row)
    except KeyError:
        return grid


def rotate_right(tile):
    new_tile = []
    n = len(tile)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(tile[n-j-1][i])
        new_tile.append(''.join(row))
    return new_tile


def get_tile_symmetries(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile = rotate_right(tile)
        tile = tile[::-1]


def get_right_edge(tile):
    return ''.join(row[-1] for row in tile),


def get_left_edge(tile):
    return ''.join(row[0] for row in tile),


def get_bottom_edge(tile):
    return tile[-1]


def get_top_edge(tile):
    return tile[0]


def align_tiles_left_to_right(tile1, tile2):
    for candidate_tile1 in get_tile_symmetries(tile1):
        for candidate_tile2 in get_tile_symmetries(tile2):
            if get_right_edge(candidate_tile1) == get_left_edge(candidate_tile2):
                return candidate_tile1, candidate_tile2

    print('\n'.join(tile1))
    print('\n')
    print('\n'.join(tile2))
    raise Exception('Could not orient tiles')


def align_tiles_top_to_bottom(tile1, tile2):
    for candidate_tile1 in get_tile_symmetries(tile1):
        for candidate_tile2 in get_tile_symmetries(tile2):
            if get_bottom_edge(candidate_tile1) == get_top_edge(candidate_tile2):
                return candidate_tile1, candidate_tile2


def build_image(ids, tiles):
    tile1, tile2 = align_tiles_left_to_right(
        tiles[ids[0][0]],
        tiles[ids[0][1]]
    )
    tiles[ids[0][0]] = tile1

    vertical_ids = list(row[0] for row in ids)
    for (id1, id2) in zip(vertical_ids, vertical_ids[1:]):
        tile1, tile2 = align_tiles_top_to_bottom(tiles[id1], tiles[id2])
        tiles[id2] = tile2

    for row in ids:
        for (id1, id2) in zip(row, row[1:]):
            tile1, tile2 = align_tiles_left_to_right(tiles[id1], tiles[id2])
            tiles[id2] = tile2

    for id_row in ids:
        for id_ in id_row:
            tiles[id_] = [
                ''.join(row[1:-1])
                for row in tiles[id_][1:-1]
            ]

    nested_tiles = [
        [tiles[id_] for id_ in id_row]
        for id_row in ids
    ]

    image = []
    for tiles_row in nested_tiles:
        for row in tiles_row[0]:
            image.append('')

    for (i, tiles_row) in enumerate(nested_tiles):
        tile_height = len(tiles_row[0])
        for tile in tiles_row:
            for (k, row) in enumerate(tile):
                image[i * tile_height + k] += row

    return image


SEA_MONSTER_PATTERNS = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]


def find_sea_monster_orientation(original_image):
    for image in get_tile_symmetries(original_image):
        for i in range(len(image) - 2):
            for j in range(len(image[0])):
                if all(
                    re.match('^{}'.format(pattern), image[i+k][j:])
                    for k, pattern in enumerate(SEA_MONSTER_PATTERNS)
                ):
                    return image


def strip_sea_monster(image, i, j):
    image = image.copy()
    for k, pattern in enumerate(SEA_MONSTER_PATTERNS):
        new_row = [c for c in image[i+k]]
        for l, c in enumerate(pattern):
            if c == '#':
                new_row[j+l] = 'O'
        image[i + k] = ''.join(new_row)
    return image


def find_sea_monsters(original_image):
    image = find_sea_monster_orientation(original_image)
    for i in range(len(image) - 2):
        for j in range(len(image[0])):
            if all(
                re.match('^{}'.format(pattern), image[i+k][j:])
                for k, pattern in enumerate(SEA_MONSTER_PATTERNS)
            ):
                image = strip_sea_monster(image, i, j)
    return image


def count_waves(image):
    count = 0
    for row in image:
        for c in row:
            if c == '#':
                count += 1
    return count


def main():
    """
    "...the outermost edges won't line up with any other tiles."
    This solution uses the uniqueness of edge-matches to find the matches.

    ...not the best code, but hey, it works.
    """
    tiles = parse_input()
    borders = build_borders(tiles)
    adjacencies = find_adjacencies(borders)
    ids = arrange_ids(adjacencies)

    corners = [
        ids[0][0],
        ids[0][-1],
        ids[-1][0],
        ids[-1][-1],
    ]
    prod = 1
    for corner in corners:
        prod *= corner
    print('Multiple of corners:', prod)

    image = build_image(ids, tiles)
    sea_monsters = find_sea_monsters(image)
    print('\n'.join(sea_monsters))

    waves = count_waves(sea_monsters)
    print('Count of waves:', waves)


main()
