# to return the cube of a number
def cube(i: int) -> int:
    return i * i * i


# use the function in list comprehension
cubes = [cube(i) for i in range(1, 6)]
print(cubes)

