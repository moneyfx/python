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

A = [11, 13, 14, 15, 17, 19, 22, 25, 36, 100]
r, i = binary_search(A, 13, 0, len(A) - 1)
print(r, i) # True 1
