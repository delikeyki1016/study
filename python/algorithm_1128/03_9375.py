# https://www.acmicpc.net/problem/9375 패션왕 신해빈
# 경우의 수 구하는 법 
# 3가지 경우 and 2가지 경우 ==> (3+1) * (2+1) - 1 ==> 11

# 1번 방법
# import sys
# TEST_CASE = int(sys.stdin.readline())

# for i in range(TEST_CASE):
#     N = int(sys.stdin.readline())
#     wear_dict = {}
#     for j in range(N):
#         item, cate = sys.stdin.readline().split()
#         if cate in wear_dict:
#             wear_dict[cate].append(item)
#         else:
#             wear_dict[cate] = []
#             wear_dict[cate].append(item)
#     print(wear_dict)
#     result = 1
#     for k in wear_dict:
#         result *= len(wear_dict[k]) + 1
#     result -= 1

#     print(result)
    
    
# default dict 이용
# import sys
# from collections import defaultdict

# TEST_CASE = int(sys.stdin.readline())

# for i in range(TEST_CASE):
#     N = int(sys.stdin.readline())
#     wear_dict = defaultdict(list)
#     for j in range(N):
#         item, cate = sys.stdin.readline().split()
#         wear_dict[cate].append(item)           
#     print(wear_dict)
#     result = 1
#     for k in wear_dict:
#         result *= len(wear_dict[k]) + 1
#     result -= 1

#     print(result)


# Counter 이용
import sys
from collections import Counter

TEST_CASE = int(sys.stdin.readline())

for i in range(TEST_CASE):
    N = int(sys.stdin.readline())
    wear = []
    for j in range(N):
        item, cate = sys.stdin.readline().split()
        wear.append(cate)           
    wear_Counter = Counter(wear)
    print(wear_Counter)
    result = 1
    for k in wear_Counter:
        result *= wear_Counter[k] + 1
    result -= 1

    print(result)