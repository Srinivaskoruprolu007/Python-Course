# let's extract the unique vowels from a string
sentence = "hello everyone"
unique_vowels = {i for i in sentence if i in 'aeiou'}
print(unique_vowels)
# here we're using set because we want unique values only

# let's use list comprehension using dictionary
squared = {i: i * i for i in range(10)}
print(squared)