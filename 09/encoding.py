from pprint import pprint


def parse_input():
    numbers = []
    try:
        while True:
            numbers.append(int(input()))
    except EOFError:
        pass
    return numbers


def is_pair_sum(trial_numbers, number):
    for x in trial_numbers:
        if number - x in trial_numbers:
            return True
    return False


def find_first_bad_number(numbers, preamble_length):
    for i in range(preamble_length, len(numbers)):
        trial_numbers = set(numbers[i - preamble_length:i])
        if not is_pair_sum(trial_numbers, numbers[i]):
            return numbers[i]


def get_contiguous_set_adding_to(numbers, target):
    totals = []
    total = 0
    for number in numbers:
        total += number
        totals.append(total)

    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers)):
            if totals[j] - totals[i] == target:
                return set(numbers[i+1:j+1])


numbers = parse_input()
bad_number = find_first_bad_number(numbers, 25)
contiguous_set = get_contiguous_set_adding_to(numbers, bad_number)
print(
    'Min/max/sum:',
    min(contiguous_set),
    max(contiguous_set),
    min(contiguous_set) + max(contiguous_set)
)
