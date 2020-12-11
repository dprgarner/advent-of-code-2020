from pprint import pprint


def parse_input():
    numbers = [0]
    try:
        while True:
            numbers.append(int(input()))
    except EOFError:
        pass
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers


def get_differences(numbers):
    deltas = {
        1: 0,
        2: 0,
        3: 0,
    }
    for i, j in zip(numbers, numbers[1:]):
        deltas[j - i] += 1
    return deltas


numbers = parse_input()
differences = get_differences(numbers)
print('1-jolt deltas times 3-jolt deltas:', differences[1] * differences[3])


def get_next_block(numbers):
    for i in range(len(numbers) - 2):
        if numbers[i + 2] - numbers[i] > 3:
            return numbers[:i + 2]
    return numbers


cache = {
    '0': 1,
    '0-1': 1,
    '0-2': 1,
    '0-3': 1,
}


def count_paths_in_block(block):
    # A block is a group of numbers where the first number _must_ be in a valid path.
    numbers = [n - block[0] for n in block]
    key = '-'.join(str(n) for n in numbers)
    if key in cache:
        # print(str(cache[key]), ' paths through block:', block)
        return cache[key]

    # There must exist solutions without numbers[1], otherwise numbers[2] would
    # not be in the same block as numbers[0].
    cache[key] = (
        count_paths_in_block(block[1:]) + count_paths_in_block(block[2:])
    )
    # There _may_ exist solutions without numbers[2], as well.
    if len(block) > 3 and block[3] - block[0] <= 3:
        cache[key] += count_paths_in_block(block[3:])

    # print(str(cache[key]), ' paths through block:', block)
    return cache[key]


def count_paths(numbers):
    if len(numbers) == 1:
        return 1
    block = get_next_block(numbers)
    return (
        count_paths_in_block(block) * count_paths(numbers[len(block) - 1:])
    )


block = get_next_block(numbers)
# print('First block:', block)
# print('Paths in block:', count_paths_in_block(block))

print('Paths:', count_paths(numbers))
