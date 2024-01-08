# 숫자리스트를 2개 받아와서 두번째 리스트안의 숫자가 첫번째리스트에 있는지 확인, 있으면 1출력 없으면 0 출력
import sys

def get_num():
    # int(sys.stdin.readline()) 문제때문에 들어있는 항목 
    return [int(i) for i in sys.stdin.readline().split()]

# def find_num(num_list1, num_list2):
#     for i in num_list2:
#         for j in num_list1:
#             if i == j:
#                 print(1)
#                 break
#         else:
#             print(0)

# num_list1 = get_num()
# num_list2 = get_num()
# find_num(num_list1, num_list2)

# i in list 로 실행
def find_num2(num_list1, num_list2):
    for i in num_list2:
        if i in num_list1:
            print(1)
        else:
            print(0)

num_list1 = get_num()
num_list2 = get_num()
find_num2(num_list1, num_list2)