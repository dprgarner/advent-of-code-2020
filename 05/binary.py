from pprint import pprint


def parse_input():
    seats = []
    try:
        while True:
            seats.append(input())
    except EOFError:
        pass
    return seats


def get_row_col(seat_string):
    row = int(
        seat_string[0:7].replace('F', '0').replace('B', '1'),
        2
    )
    col = int(
        seat_string[7:].replace('L', '0').replace('R', '1'),
        2
    )
    return row, col


def get_seat_id(seat_string):
    row, col = get_row_col(seat_string)
    return 8 * row + col


def get_missing_seat_id(seats):
    seats_set = set(seats)
    min_seat_id = min(seats)
    max_seat_id = max(seats)
    for i in range(min_seat_id, max_seat_id):
        if i not in seats_set:
            return i


seats = [
    get_seat_id(seat)
    for seat in parse_input()
]

print('Max seat ID:', max(seats))
print('missing seat:', get_missing_seat_id(seats))
