"""" linear search is an algorithm which is used to search the element
    in this algorithm the item will be searched in linearly"""


def search(array: bytearray, x: int) -> int:
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1


arr = bytearray([1, 4, 6, 8, 9])
num = 8
print(search(arr, num))

# time complexity of this algorithm is O(n)
# Auxiliary space of this algorithm is O(1)
