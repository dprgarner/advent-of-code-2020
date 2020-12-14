from pprint import pprint
import math
from crt import chinese_remainder_theorem


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
