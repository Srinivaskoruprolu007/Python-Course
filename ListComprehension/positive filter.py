# filter the numbers from a list
All_numbers = [1, 5, 3, 7, 8, -3, -4, 6, -3, -6, -44]
positives = [i for i in All_numbers if i > 0]
negitive = [i for i in All_numbers if i < 0]
print(negitive)
print(positives)
