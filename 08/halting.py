from pprint import pprint


def parse_input():
    commands = []
    try:
        while True:
            command, amount = input().split(' ')
            commands.append((command, int(amount)))
    except EOFError:
        pass
    return commands


def run_until_repeat_or_complete(commands):
    total = 0
    commands_executed = set()
    current = 0

    while current not in commands_executed:
        if current == len(commands):
            return True, total
        commands_executed.add(current)
        command, amount = commands[current]
        if command == 'nop':
            current += 1
        elif command == 'acc':
            total += amount
            current += 1
        elif command == 'jmp':
            current += amount
        else:
            raise Exception('unknown command')

    return False, total


def find_corrected_total(commands):
    for i, (command, total) in enumerate(commands):
        if command == 'acc':
            continue
        modified_commands = commands.copy()
        modified_commands[i] = ('jmp' if command == 'nop' else 'nop', total)
        is_complete, amount = run_until_repeat_or_complete(modified_commands)
        if is_complete:
            print('Modified step: ', i)
            return amount


commands = parse_input()


print(
    'Original corrupt program total: ',
    run_until_repeat_or_complete(commands)[1]
)

print(
    'Corrected program:',
    find_corrected_total(commands)
)
