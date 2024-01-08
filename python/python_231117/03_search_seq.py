def find_my_num(list, value):
    """해당 함수를 help(find_my_num)를 했을 때 나오는 가이드

    Args:
        list (_type_): 입력받을 list
        value (_type_): 찾고자 하는 숫자 

    Returns:
        _type_: 찾으면 해당 라인index, 없으면 -1 리턴 
    """
    for i in range(len(list)):
        if value == list[i]:
            return i
    return -1
        
print(find_my_num([5,4,3,1,2], 3))

help(find_my_num)

# def find2(list):
#     for i in list:
#         print(i)
#     return i # return을 안써주면 none이 출력된다. 

# print(find2([1,2,3]))