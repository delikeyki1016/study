# 피벗정렬(퀵정렬)
# left가 pivet보다 클때까지  이동
# right가 pivet보다 작을때까지 이동 
# 한 후 스왑 
# right, left가 바뀌면 right가 피벗

arr = [10, 55, 17, 25, 22]

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[start]:
            left += 1
        while right > start and arr[right] >= arr[start]:
            right -= 1
        if left > right:
            arr[start], arr[right] = arr[right], arr[start]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    print(arr)
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)