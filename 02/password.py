from pprint import pprint
import re


def parse_input():
    passwords = []
    try:
        while True:
            input_match = re.match(r'(\d+)-(\d+) (\w): (\w+)', input())
            passwords.append((
                int(input_match[1]),
                int(input_match[2]),
                input_match[3],
                input_match[4],
            ))
    except EOFError:
        pass
    return passwords


def is_valid_min_max(min_, max_, char, password):
    count = 0
    for c in password:
        if c == char:
            count += 1

    return count >= min_ and count <= max_


def count_valid_min_max_passwords(passwords):
    count = 0
    for password in passwords:
        if is_valid_min_max(*password):
            count += 1
    return count


def is_valid_position(must, never, char, password):
    if never > len(password):
        raise Exception('Invalid input')
    return (
        password[must - 1] == char and password[never - 1] != char or
        password[must - 1] != char and password[never - 1] == char
    )


def count_valid_position_passwords(passwords):
    count = 0
    for password in passwords:
        if is_valid_position(*password):
            count += 1
    return count


passwords = parse_input()
print(
    'Valid passwords with rule set 1:',
    count_valid_min_max_passwords(passwords)
)
print(
    'Valid passwords with rule set 2:',
    count_valid_position_passwords(passwords)
)
