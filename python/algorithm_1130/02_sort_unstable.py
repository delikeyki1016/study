log = [['서울', '09:00:00'],
['대전', '09:00:03'],
['대구', '09:00:13'],
['서울', '09:00:59'],
['대구', '09:01:10'],
['서울', '09:03:13'],
['부산', '09:10:11'],
['부산', '09:10:25'],
['대전', '09:14:25'],
['서울', '09:19:32'],
['서울', '09:19:46'],
['서울', '09:21:05'],
['부산', '09:22:43'],
['부산', '09:22:54'],
['서울', '09:25:52'],
['서울', '09:35:21'],
['부산', '09:36:14'],
['대전', '09:37:44']]

# 퀵정렬은 불안정정렬
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
    # print(arr)
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

# print(quick_sort(log, 0, len(log) - 1))

from pprint import pprint
pprint(quick_sort(log, 0, len(log) - 1))