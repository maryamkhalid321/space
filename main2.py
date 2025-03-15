def bim(arr, tar):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == tar:
            return mid
        elif tar < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
target = 7
result = bim(arr, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
