def binary_search(arr: list[int], x: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    mid: int = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

# function call
result:int = binary_search(arr,x)
if result != 1:
    print("Element is present a index",result)
else:
    print("Element is not present in array")