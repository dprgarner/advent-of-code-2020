def parse_input():
    moves, total_cups = (int(s) for s in input().split(' '))
    input_ints = [int(x) for x in input()]
    input_ints = input_ints + list(range(len(input_ints) + 1, total_cups + 1))
    cups = {}
    for i, j in zip(input_ints, input_ints[1:] + [input_ints[0]]):
        cups[i] = j
    return moves, cups, input_ints[0]


def iterate(cups, current_cup):
    next1 = cups[current_cup]
    next2 = cups[next1]
    next3 = cups[next2]
    cups[current_cup] = cups[next3]

    destination = current_cup
    while destination in {current_cup, next1, next2, next3}:
        destination -= 1
        if destination == 0:
            destination = len(cups)
    cups[next3] = cups[destination]
    cups[destination] = next1

    return cups, cups[current_cup]


def get_string_from_one(cups):
    next_cup = cups[1]
    ordered_cups = []
    while next_cup != 1:
        ordered_cups.append(str(next_cup))
        next_cup = cups[next_cup]
    return ''.join(ordered_cups)


def print_product(cups):
    first_cup = cups[1]
    second_cup = cups[first_cup]
    print('First two cups: {} {}'.format(first_cup, second_cup))
    print('Product:', first_cup * second_cup)


def main():
    """
    Runs in ~10 seconds. Much slower than C++, but hey, at least it's not C++.
    """
    moves, cups, current_cup = parse_input()
    for _ in range(moves):
        # print(current_cup, ':', cups)
        # print(get_string_from_one(cups))
        cups, current_cup = iterate(cups, current_cup)
    if len(cups) < 10:
        print(
            'Final after {} moves: {}'.format(moves, get_string_from_one(cups))
        )
    print_product(cups)


main()
