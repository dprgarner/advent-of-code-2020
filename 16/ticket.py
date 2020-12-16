from pprint import pprint


def parse_input():
    rules = {}
    try:
        line = input()
        while line:
            k, v = line.split(': ')
            # Every v is of the form "42-259 or 269-974"
            ranges = v.split(' or ')
            rules[k] = [
                tuple([int(s) for s in range_.split('-')])
                for range_ in ranges
            ]
            line = input()

        assert input() == 'your ticket:'
        ticket = [int(s) for s in input().split(',')]

        assert not input()
        assert input() == 'nearby tickets:'

        nearby_tickets = []
        line = input()
        while line:
            nearby_tickets.append([int(s) for s in line.split(',')])
            line = input()

    except EOFError:
        pass
    return rules, ticket, nearby_tickets


def is_valid_by_rule(rule, number):
    return rule[0] <= number and number <= rule[1]


def number_matches_some_rule(rules, number):
    for rule_list in rules.values():
        for rule in rule_list:
            if is_valid_by_rule(rule, number):
                return True
    return False


def get_invalid_numbers(rules, ticket):
    invalid_numbers = []
    for number in ticket:
        if not number_matches_some_rule(rules, number):
            invalid_numbers.append(number)
    return invalid_numbers


def is_valid_by_ranges(ranges, number):
    return any(is_valid_by_rule(range_, number) for range_ in ranges)


def all_numbers_valid_by_rule(ranges, numbers):
    return all(is_valid_by_ranges(ranges, number) for number in numbers)


def solve(rules, tickets):
    # For each rule: what ticket indexes are valid?
    valid_indexes = {}
    for rule, ranges in rules.items():
        valid_indexes[rule] = []

        for i in range(len(tickets[0])):
            if all_numbers_valid_by_rule(ranges, [
                ticket[i] for ticket in tickets
            ]):
                valid_indexes[rule].append(i)

    rule_indexes = {}
    while valid_indexes:
        rule = next(
            rule
            for rule, indexes in valid_indexes.items()
            if len(indexes) == 1
        )
        index = valid_indexes[rule][0]

        rule_indexes[rule] = index
        for k in valid_indexes:
            valid_indexes[k] = list(
                filter(lambda x: x != index, valid_indexes[k])
            )
        del valid_indexes[rule]

    rules_list = [None] * len(tickets[0])
    for rule, index in rule_indexes.items():
        rules_list[index] = rule
    return rules_list


def main():
    rules, my_ticket, nearby_tickets = parse_input()
    error_rate = 0
    for ticket in nearby_tickets:
        for number in get_invalid_numbers(rules, ticket):
            error_rate += number
    print('error rate:', error_rate)

    valid_tickets = [
        ticket
        for ticket in nearby_tickets
        if get_invalid_numbers(rules, ticket) == []
    ]

    field_order = solve(rules, [ticket] + valid_tickets)
    product = 1
    for rule, number in zip(field_order, my_ticket):
        if rule.startswith('departure'):
            product *= number

    print('solution:', product)


main()
