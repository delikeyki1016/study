# https://www.acmicpc.net/problem/2953
import sys

# 방법 1 
# max_sum = 0
# winner = 1
# for i in range(5):
#     scores = [int(j) for j in sys.stdin.readline().split()]
#     sum = 0
#     for k in scores:
#         sum += k
#     if sum > max_sum:
#         max_sum = sum
#         winner = i + 1
    
# print(winner, max_sum)

# 방법 2 
# scores_list = []
# for _ in range(5):
#     scores = [int(i) for i in sys.stdin.readline().split()]
#     scores_list.append(sum(scores))
# print(scores_list.index(max(scores_list)) + 1, max(scores_list))

# 방법 3
scores_list = [sum([int(i) for i in sys.stdin.readline().split()]) for _ in range(5)]
print(scores_list.index(max(scores_list)) + 1, max(scores_list))

