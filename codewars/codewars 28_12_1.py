import math


def find_next_square(sq):
    sqrt1 = math.sqrt(sq)
    return (sqrt1 + 1) ** 2 if sq % sqrt1 == 0 and sq > 0 else -1


find_next_square(121)