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


def build_rules(rules):
    rules_dict = {}
    for i, rule in rules:
        rules_dict[i] = rule
    return rules_dict


cache = {}


def matches(rules, rule, expression):
    """
    This works for the simple version, but runs _really slowly_.
    """
    if not expression:
        return True

    if type(rule) == int:
        if (rule, expression) not in cache:
            cache[(rule, expression)] = matches(rules, rules[rule], expression)
        return cache[(rule, expression)]

    if type(rule) == str:
        # Just a char-match.
        return expression == rule

    if rule == []:
        return not expression

    if type(rule[0]) == list:
        # List of ORed subrules. Any will be fine.
        return any(
            matches(rules, subrule, expression)
            for subrule in rule
        )

    # A sequence to try. Try splitting the expression down.
    for i in range(len(expression) + 1):
        if (
            matches(rules, rule[0], expression[:i]) and
            matches(rules, rule[1:], expression[i:])
        ):
            return True

    return False


def parse_input():
    rules = []
    expressions = []
    try:
        while True:
            line = input()
            if not line:
                break
            rules.append(parse_rule(line))
        while True:
            expressions.append(input())
    except EOFError:
        pass
    return build_rules(rules), expressions


def main():
    rules, expressions = parse_input()
    matching_expressions = []
    for expression in expressions:
        if matches(rules, rules[0], expression):
            matching_expressions.append(expression)
        print('.', end='', flush=True)
    print('\nNumber of matches:', len(matching_expressions))


main()
