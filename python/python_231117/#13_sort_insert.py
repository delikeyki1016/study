# 삽입정렬 : 삽입정렬이 선택정렬보다 효율적
def insertion_sorted(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

    # 이중 for문 사용
    # for i in range(1, len(list)):
    #     for j in range(i, 0, -1):
    #         if list[j] < list[j-1]:
    #             list[j], list[j-1] = list[j-1], list[j]
    #         else:
    #             break
    # return list

chars = ['d', 'a', 'b', 'c', 'e']

print(insertion_sorted(chars))