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

            bag_types[bag_type] = {}
            if 'no other' in bag_contents:
                continue

            for bag_phrase in bag_contents.split(', '):
                bag_match = re.match(r'(\d+) (.*)', bag_phrase)
                sub_bag_count = int(bag_match[1])
                sub_bag_type = bag_match[2]
                bag_types[bag_type][sub_bag_type] = sub_bag_count
    except EOFError:
        pass
    return bag_types


def bags_to_sets(bag_counts):
    return {
        bag_type: set(bag_contents.keys())
        for bag_type, bag_contents in bag_counts.items()
    }


def find_types_which_hold(bags, good_bag_type):
    good_types = set()
    for bag_type, bag_contents in bags.items():
        if good_bag_type in bag_contents:
            good_types.add(bag_type)

    recursive_types = good_types.copy()
    for bag_type in good_types:
        recursive_types.update(find_types_which_hold(bags, bag_type))

    return recursive_types


# Assumes no bag ever contains itself, otherwise this question is not well-posed
def recursive_count_total_bags(bags, inner_bags):
    total = 1
    for bag_type, sub_bag_total in inner_bags.items():
        total += (
            sub_bag_total * recursive_count_total_bags(bags, bags[bag_type])
        )
    return total


def count_total_bags_containing(bags, good_bag_type):
    return recursive_count_total_bags(bags, bags[good_bag_type]) - 1


def main():
    bag_counts = parse_bags()
    bag_sets = bags_to_sets(bag_counts)
    print(
        'Bags which could have a shiny gold bag:',
        len(find_types_which_hold(bag_sets, 'shiny gold'))
    )
    print(
        'Total bags in a shiny gold bag:',
        count_total_bags_containing(bag_counts, 'shiny gold')
    )


main()
