def parse_input():
    expressions = []
    try:
        while True:
            expressions.append(input())
    except EOFError:
        pass
    return expressions


def tokenise(expression):
    """
    Tokenises the expression into a tree.

    This approach tokenises by recursion and by splitting up the expression on
    the operators of least precedence first. In particular, operators in
    brackets must be tokenised after operators outside of brackets, and
    lower-precendence operators are parsed before higher-precendence ones.
    expression = expression.replace(' ', '')

    This code is adapted from an earlier Kata I did on this.
    """
    parenthesis_count = 0
    expression = expression.strip()

    for i in range(len(expression)-1, -1, -1):
        c = expression[i]
        if c == ')':
            parenthesis_count += 1
        if c == '(':
            parenthesis_count -= 1
        if parenthesis_count:
            continue

        if c == '*':
            return c, tokenise(expression[:i]), tokenise(expression[i+1:])

    for i in range(len(expression)-1, -1, -1):
        c = expression[i]
        if c == ')':
            parenthesis_count += 1
        if c == '(':
            parenthesis_count -= 1
        if parenthesis_count:
            continue

        if c == '+':
            return c, tokenise(expression[:i]), tokenise(expression[i+1:])

    if expression[0] == '(' and expression[-1] == ')':
        return tokenise(expression[1:-1])

    return int(expression)


def evaluate(token):
    if not isinstance(token, tuple):
        return token

    operator, operand1, operand2 = token
    if operator == '+':
        return evaluate(operand1) + evaluate(operand2)
    if operator == '*':
        return evaluate(operand1) * evaluate(operand2)

    raise Exception('Unknown operation:', token)


def calc(expression):
    token = tokenise(expression)
    return evaluate(token)


def main():
    expressions = parse_input()
    print('Result:', sum(
        calc(expression)
        for expression in expressions
    ))


main()
