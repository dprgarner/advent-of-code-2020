from pprint import pprint


def parse_input():
    groups = []
    group = []
    try:
        while True:
            line = input()
            if not line:
                groups.append(group)
                group = []
                continue
            group.append(line)
    except EOFError:
        pass
    groups.append(group)
    return groups


def get_unique_answers(group):
    group_answers = set()
    for person in group:
        for answer in person:
            group_answers.add(answer)
    return group_answers


def get_everyone_answered(group):
    unique_group_answers = get_unique_answers(group)
    unanimous_answers = set()
    for answer in unique_group_answers:
        if all([answer in person for person in group]):
            unanimous_answers.add(answer)
    return unanimous_answers


groups = parse_input()
print(
    'Sum of unique answer counts:',
    sum([
        len(get_unique_answers(group))
        for group in groups
    ])
)

print(
    'Sum of unanimous answer counts:',
    sum([
        len(get_everyone_answered(group))
        for group in groups
    ])
)
