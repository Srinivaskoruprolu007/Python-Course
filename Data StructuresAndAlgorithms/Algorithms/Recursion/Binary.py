def binary_search(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
y = 40

result = binary_search(arr, 0, len(arr)-1, y)
if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")
