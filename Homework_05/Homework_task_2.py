def generate_natural_cubes(n: int):
    a = [i ** 3 for i in range(1, n + 1)]
    return a


assert generate_natural_cubes(3) == [1, 8, 27]
assert generate_natural_cubes(5) == [1, 8, 27, 64, 125]
