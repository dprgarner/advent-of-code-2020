import re
from pprint import pprint


def parse_input():
    passports = []
    passport = {}
    try:
        while True:
            line = input()
            if not line:
                passports.append(passport)
                passport = {}
                continue

            for field_string in line.split(' '):
                k, v = field_string.split(':')
                if k != 'cid':
                    passport[k] = v
    except EOFError:
        pass
    passports.append(passport)
    return passports


def has_correct_fields(passport):
    return set(passport) == set([
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    ])


def is_in_range(value, min_, max_):
    return value >= min_ and value <= max_


def is_valid_height(height):
    cm_match = re.match(r'(\d+)cm', height)
    if cm_match:
        height_cm = int(cm_match[1])
        return height_cm >= 150 and height_cm <= 193
    in_match = re.match(r'(\d+)in', height)
    if in_match:
        height_in = int(in_match[1])
        return height_in >= 59 and height_in <= 76
    return False


def is_valid(passport):
    if not has_correct_fields(passport):
        return False

    return all([
        is_in_range(int(passport['byr']), 1920, 2002),
        is_in_range(int(passport['iyr']), 2010, 2020),
        is_in_range(int(passport['eyr']), 2020, 2030),
        is_valid_height(passport['hgt']),
        re.match(r'^#[a-f0-9]{6}$', passport['hcl']),
        passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        re.match(r'^[0-9]{9}$', passport['pid']),
    ])


passports = parse_input()
print(
    'Passports with correct fields:',
    sum([has_correct_fields(passport)for passport in passports])
)
print(
    'Strictly-valid passports:',
    sum([is_valid(passport)for passport in passports])
)
