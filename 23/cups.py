def parse_input():
    moves = int(input())
    return moves, [int(x) for x in input()]


def iterate(cups):
    n = max(cups)
    cups = cups.copy()
    current = cups.pop(0)
    cups.append(current)
    moving, cups = cups[:3], cups[3:]

    destination = current
    while True:
        destination -= 1
        if destination == 0:
            destination = n
        if destination in cups:
            break
    idx = cups.index(destination)
    return cups[:idx + 1] + moving + cups[idx + 1:]


def get_string(cups):
    if cups[-1] != 1:
        idx = cups.index(1)
        cups = cups[idx + 1:] + cups[:idx + 1]
    return ''.join(str(i) for i in cups[:-1])


def main():
    """
    Just the first solution.
    """
    moves, cups = parse_input()
    for _ in range(moves):
        cups = iterate(cups)
    print('Final after {} moves: {}'.format(moves, get_string(cups)))


main()

# Wrong answer: 389257641
