import math
from crt import get_bezout_coefficients


def check_prime(n):
    for k in range(2, math.floor(math.sqrt(n))):
        if n % k == 0:
            raise Exception('{} is not prime: {}'.format(n, k))


def invert(subject, n):
    inverse = get_bezout_coefficients(subject, n)[0]
    while inverse < 0:
        inverse += n
    assert (subject * inverse) % n == 1
    return inverse


def exponentiate_to_one(n, coefficient, base):
    # Find c s.t. coefficient * base ** c == 1 (mod n)
    c = 0
    prod = coefficient
    while prod != 1:
        prod = (prod * base) % n
        c += 1
    return c


def exponentiate(n, base, power):
    x = base
    prod = 1
    for c in '{:b}'.format(power)[::-1]:
        if c == '1':
            prod = (prod * x) % n
        x = (x * x) % n
    return prod


def main(n, card_public, door_public):
    for k in range(2, math.floor(math.sqrt(n))):
        if n % k == 0:
            raise Exception('{} is not prime: {}'.format(n, k))

    inverse = invert(7, n)
    print('Inverse:', inverse)

    # Look for c s.t 7**c == card_public
    # i.e card_public * (inverse)**c == 1
    c = exponentiate_to_one(n, card_public, inverse)
    print('c:', c)

    encryption_key = exponentiate(n, door_public, c)
    print('encryption key:', encryption_key)


# "Small" values
# card_public = 5764801
# door_public = 17807724

# "Large" values
card_public = 10943862
door_public = 12721030

main(20201227, card_public, door_public)
