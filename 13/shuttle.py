from pprint import pprint
import math


def parse_input():
    time = int(input())
    departures = [
        None if str_ == 'x' else int(str_)
        for str_ in input().split(',')
    ]
    return (time, departures)


def next_bus_and_wait(time, departures):
    next_time = None
    next_bus = None
    for bus in departures:
        if not bus:
            continue
        candidate_time = math.ceil(time / bus) * bus
        if not next_time or candidate_time < next_time:
            next_time = candidate_time
            next_bus = bus
    return next_bus, next_time - time


def get_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


def get_euclid_coefficients(a, b):
    # Assume a, b coprime, a > b.
    x = a // b
    r = a % b
    if r == 0:
        return [x]
    return [x] + get_euclid_coefficients(b, r)


def get_bezout_coefficients(a, b):
    # Assumes a > b, a and b are coprime.
    # Find x, y s.t. a * x + b * y == 1
    if a < b:
        raise Exception('a < b')

    cs = get_euclid_coefficients(a, b)[::-1][1:]
    x, y = 1, -1 * cs[0]
    for c in cs[1:]:
        x, y = y, x - (y * c)

    assert a * x + b * y == 1
    return x, y


def chinese_remainder_theorem(congruences):
    # Each entry (a, m) is a congruence of the form:
    # x % m == a
    # All m are assumed to be coprime.
    product = get_product(coprime for _, coprime in congruences)
    moduli = [product // coprime for _, coprime in congruences]
    bezout_coefficients = [
        get_bezout_coefficients(n, p)
        for (_, p), n in zip(congruences, moduli)
    ]
    solution_coefficients = [
        (a, c, m)
        for (a, _), m, (c, _) in zip(congruences, moduli, bezout_coefficients)
    ]
    solution = sum(a * c * m for a, c, m in solution_coefficients)
    while solution < 0:
        solution += product
    return (solution % product)


def get_congruences(departures):
    congruences = []
    for i, bus in enumerate(departures):
        if not bus:
            continue
        coefficient = -i
        while coefficient < 0:
            coefficient += bus
        congruences.append((coefficient, bus))
    return congruences


def main():
    time, departures = parse_input()
    bus, wait = next_bus_and_wait(time, departures)
    print('Wait for next bus:', bus, wait)
    print('bus * wait:', bus * wait)

    congruences = get_congruences(departures)
    solution = chinese_remainder_theorem(congruences)
    print('Solution:', solution)


main()
