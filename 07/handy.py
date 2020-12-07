import pprint
import re


def parse_bags():
    bag_types = {}

    try:
        while True:
            bag_type, bag_contents = (
                input()
                .replace(' bags', '')
                .replace(' bag', '',)
                .replace('.', '')
                .split(' contain ')
            )
            if bag_type in bag_types:
                raise Exception('Duplicate key')

            bag_types[bag_type] = set()

            if 'no other' in bag_contents:
                continue

            for bag_phrase in bag_contents.split(', '):
                bag_match = re.match(r'(\d+) (.*)', bag_phrase)
                # bag_count = int(bag_match[1])
                bag_colour = bag_match[2]
                # bag_types[bag_type][bag_colour] = bag_count
                bag_types[bag_type].add(bag_colour)

    except EOFError:
        pass
    return bag_types


def find_colours_which_hold(bags, good_bag_type):
    good_colours = set()
    for bag_type, bag_contents in bags.items():
        if good_bag_type in bag_contents:
            good_colours.add(bag_type)
            # del bags[bag_type]

    recursive_colours = good_colours.copy()
    for colour in good_colours:
        recursive_colours.update(find_colours_which_hold(bags, colour))

    return recursive_colours


print(len(find_colours_which_hold(parse_bags(), 'shiny gold')))
