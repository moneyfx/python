def binary_search(arr, target, start, end):
    if start > end:
        return False, None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return True, mid
    
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)

arr = [11, 13, 14, 15, 17, 19, 22, 25, 36, 100]
print(binary_search(arr, 100, 0, len(arr) - 1))
