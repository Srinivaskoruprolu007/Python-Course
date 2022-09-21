"""" this is similar to linear search but
the only difference is instead of iterative
 we're using recursive Approach"""

""" Recursion :
Recursion is the process where the function 
calling itself in the function only"""


# linear Search

def linear_search(array: bytearray, num: int, index: int) -> int:
    if index == -1:
        return -1
    if array[index] == num:
        return index
    return linear_search(array, num, index-1)


number = bytearray([1, 5, 7, 3, 8, 0, 88])
element = 8
print(linear_search(number, element, len(number)-1))

# time complexity = O(n)
# space complexity = O(n)
