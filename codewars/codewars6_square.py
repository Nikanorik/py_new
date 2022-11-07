import math


def is_square(n):
    if n < 0:
        return False
    else:
        square_number = int(math.sqrt(n))
        if square_number ** 2 == n:
            return True
        else:
            return False


is_square(-1)