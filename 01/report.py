
def parse_input():
    entries = []
    try:
        while True:
            entries.append(int(input()))
    except EOFError:
        pass
    return entries


def get_pair_totalling(numbers, quantity):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == quantity:
                return numbers[i], numbers[j]


def get_triple_totalling(numbers, quantity):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == quantity:
                    return numbers[i], numbers[j], numbers[k]


entries = parse_input()
x, y = get_pair_totalling(entries, 2020)
print('Pair:', x * y)


x, y, z = get_triple_totalling(entries, 2020)
print('Triple:', x * y * z)
