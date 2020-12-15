from pprint import pprint


def parse_input():
    return [int(i) for i in input().split(',')]


def iterate_until(starting_numbers, target):
    lookup_last = {}
    for i, n in enumerate(starting_numbers[:-1]):
        lookup_last[n] = i + 1

    last = starting_numbers[-1]
    for i in range(len(starting_numbers), target):
        if last in lookup_last:
            new_last = i - lookup_last[last]
        else:
            new_last = 0
        lookup_last[last] = i
        last = new_last

    return last


def main():
    starting_numbers = parse_input()
    print(iterate_until(starting_numbers, 30000000))


main()
