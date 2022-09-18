# function with Arbitrary number of parameters

def sum_of_all_nums(*num:int) -> int:
    total = 0
    for i in num:
        total += i
    return total

print(sum_of_all_nums(3,5,7,2,7))