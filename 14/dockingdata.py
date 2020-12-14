from pprint import pprint


def parse_input():
    commands = []
    try:
        while True:
            line = input()
            if line.startswith('mask = '):
                commands.append(('SET_MASK', line.replace('mask = ', '')))
            else:
                address = int(line.split('[')[1].split(']')[0])
                value = int(line.split(' = ')[1])
                commands.append(('SET_MEMORY', address, value))
    except EOFError:
        pass
    return commands


def to_36_bit(value):
    return '{:36b}'.format(value).replace(' ', '0')


def set_v1_masked_bits(mask, value):
    str_binary = to_36_bit(value)
    return ''.join(
        c
        if m == 'X'
        else m
        for c, m in zip(str_binary, mask)
    )


def run_v1_program(commands):
    memory = {}
    mask = None
    for command in commands:
        if command[0] == 'SET_MASK':
            mask = command[1]
        if command[0] == 'SET_MEMORY':
            _, address, value = command
            memory[address] = set_v1_masked_bits(mask, value)
    return memory


def expand_address(floating_address):
    if 'X' not in floating_address:
        return [floating_address]
    idx = floating_address.find('X')
    return (
        expand_address(floating_address[:idx] + '0' + floating_address[idx+1:]) +
        expand_address(floating_address[:idx] + '1' + floating_address[idx+1:])
    )


def get_addresses(mask, address):
    str_binary = to_36_bit(address)
    floating_address = ''.join(
        c
        if m == '0'
        else m
        for c, m in zip(str_binary, mask)
    )
    return [
        int(s, 2) for s in expand_address(floating_address)
    ]


def run_v2_program(commands):
    memory = {}
    mask = None
    for command in commands:
        if command[0] == 'SET_MASK':
            mask = command[1]
        if command[0] == 'SET_MEMORY':
            _, address, value = command
            for modified_address in get_addresses(mask, address):
                memory[modified_address] = value
    return memory


def v1_sum_in_memory(memory):
    return sum(int(s, 2) for s in memory.values())


def v2_sum_in_memory(memory):
    return sum(v for v in memory.values())


commands = parse_input()
memory = run_v1_program(commands)
print('Total v1 sum:', v1_sum_in_memory(memory))
memory = run_v2_program(commands)
print('Total v2 sum:', v2_sum_in_memory(memory))
