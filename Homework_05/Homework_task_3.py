def generate_squares(*args: int):
    a = [i ** 2 for i in args]
    return a


assert generate_squares(1, 2, 3) == [1, 4, 9]
assert generate_squares(1, 3, 5, 4, 2) == [1, 9, 25, 16, 4]
