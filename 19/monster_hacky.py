import re
from pprint import pprint


def parse_rule(expr):
    number, rule_text = expr.split(': ')
    number = int(number)
    if '"' in rule_text:
        char = rule_text[1]
        return (number, char)
    subrules = [
        [int(n) for n in subrule_str_.split(' ')]
        for subrule_str_ in rule_text.split(' | ')
    ]
    return (number, subrules)


def build_regex(rules, idx):
    rule = rules[idx]
    # This is hacky, but it's good enough to solve the problem.
    if idx == 8 and rule == [[42], [42, 8]]:
        return '({})+'.format(build_regex(rules, 42))
    if idx == 11 and rule == [[42, 31], [42, 11, 31]]:
        # Hack. I don't know of a way to write this in an arbitrary regex, so
        # this will just assume that the expressions in question are short
        # enough.
        subrule1 = build_regex(rules, 42)
        subrule2 = build_regex(rules, 31)
        return '({})'.format(
            '|'.join(
                '(({}){{{}}}({}){{{}}})'.format(subrule1, i, subrule2, i)
                for i in range(1, 10)
            )
        )

    if type(rule) == str:
        return rule
    return '({})'.format(
        '|'.join(
            ''.join(build_regex(rules, i) for i in subrule)
            for subrule in rule
        )
    )


def parse_input():
    rules = []
    expressions = []
    try:
        while True:
            line = input()
            if not line:
                break
            rules.append(parse_rule(line))
        rules_dict = {}
        for (i, rule) in rules:
            rules_dict[i] = rule
        while True:
            expressions.append(input())
    except EOFError:
        pass
    regex_str = build_regex(rules_dict, 0)
    return re.compile('^{}$'.format(regex_str)), expressions


def main():
    regex, expressions = parse_input()
    matching_expressions = []
    for expression in expressions:
        if regex.match(expression):
            matching_expressions.append(expression)
    print('\nNumber of matches:', len(matching_expressions))


main()
