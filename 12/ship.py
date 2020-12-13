from pprint import pprint


def parse_input():
    actions = []
    try:
        while True:
            line = input()
            actions.append((line[0], int(line[1:])))
    except EOFError:
        pass

    return actions


def move(position, waypoint, number):
    return (
        position[0] + waypoint[0] * number,
        position[1] + waypoint[1] * number
    )


def perform_simple_actions(actions):
    position = (0, 0)
    waypoint = (1, 0)

    for char, number in actions:
        if char == 'L':
            for _ in range(number // 90):
                waypoint = -waypoint[1], waypoint[0]
        elif char == 'R':
            for _ in range(number // 90):
                waypoint = waypoint[1], -waypoint[0]
        elif char == 'F':
            position = move(position, waypoint, number)
        elif char == 'N':
            position = move(position, (0, 1), number)
        elif char == 'E':
            position = move(position, (1, 0), number)
        elif char == 'S':
            position = move(position, (0, -1), number)
        elif char == 'W':
            position = move(position, (-1, 0), number)
    return position


def perform_waypoint_actions(actions):
    position = (0, 0)
    waypoint = (10, 1)

    for char, number in actions:
        if char == 'L':
            for _ in range(number // 90):
                waypoint = -waypoint[1], waypoint[0]
        elif char == 'R':
            for _ in range(number // 90):
                waypoint = waypoint[1], -waypoint[0]
        elif char == 'F':
            position = move(position, waypoint, number)
        elif char == 'N':
            waypoint = move(waypoint, (0, 1), number)
        elif char == 'E':
            waypoint = move(waypoint, (1, 0), number)
        elif char == 'S':
            waypoint = move(waypoint, (0, -1), number)
        elif char == 'W':
            waypoint = move(waypoint, (-1, 0), number)
    return position


def manhattan(position):
    return abs(position[0]) + abs(position[1])


actions = parse_input()
simple_final_position = perform_simple_actions(actions)
print('Simple final position:', simple_final_position)
print('Manhattan distance:', manhattan(simple_final_position))

waypoint_final_position = perform_waypoint_actions(actions)
print('Waypoint final position:', waypoint_final_position)
print('Manhattan distance:', manhattan(waypoint_final_position))
