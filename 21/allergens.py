def parse_input():
    foods = []
    try:
        while True:
            line = input()
            ingredients_str, allergens_str = line.split(' (contains ')
            ingredients = set(ingredients_str.split(' '))
            allergens = set(allergens_str.replace(')', '').split(', '))
            foods.append((ingredients, allergens))
    except EOFError:
        pass
    return foods


def intersection(sets):
    final_set = sets[0]
    for set_ in sets[1:]:
        final_set = final_set.intersection(set_)
    return final_set


def find_ingredient_with_allergen(foods):
    all_allergens = set()
    all_ingredients = set()
    for i, a in foods:
        all_ingredients.update(i)
        all_allergens.update(a)

    for allergen in all_allergens:
        candidate_ingredients = []
        for ingredients, allergen_list in foods:
            if allergen in allergen_list:
                candidate_ingredients.append(ingredients)
        candidate_ingredients = intersection(candidate_ingredients)

        if len(candidate_ingredients) == 1:
            return candidate_ingredients.pop(), allergen


def find_ingredient_by_allergen(original_foods):
    foods = [
        (ingredients.copy(), allergens.copy())
        for ingredients, allergens in original_foods
    ]
    ingredient_by_allergen = {}

    match = find_ingredient_with_allergen(foods)
    while match:
        ingredient, allergen = match
        for ingredients, allergens in foods:
            if ingredient in ingredients:
                ingredients.remove(ingredient)
            if allergen in allergens:
                allergens.remove(allergen)
        ingredient_by_allergen[allergen] = ingredient
        match = find_ingredient_with_allergen(foods)

    return ingredient_by_allergen


def find_unmatched_ingredients(foods, ingredient_by_allergen):
    unmatched_ingredients = set()
    for ingredients, allergens in foods:
        assert not allergens.difference(ingredient_by_allergen.keys())
        unmatched_ingredients.update(ingredients.difference(
            ingredient_by_allergen.values()
        ))

    return unmatched_ingredients


def count_occurrences(ingredients_to_find, ingredients_list):
    count = 0
    for ingredients in ingredients_list:
        count += len(ingredients.intersection(ingredients_to_find))
    return count


def main():
    foods = parse_input()

    for x in foods:
        print(x)

    ingredient_by_allergen = find_ingredient_by_allergen(foods)
    unmatched_ingredients = find_unmatched_ingredients(
        foods, ingredient_by_allergen
    )
    occurrences = count_occurrences(
        unmatched_ingredients,
        [ingredients for ingredients, _ in foods],
    )
    print('Occurrences of unmatched ingredients:', occurrences)
    print('Ingredients by allergen:', ingredient_by_allergen)
    ingredient_string = ','.join(
        x[1] for x in sorted([
            (k, v)
            for k, v in ingredient_by_allergen.items()
        ], key=lambda x: x[0])
    )
    print('sorted ingredient string:')
    print(ingredient_string)


main()
