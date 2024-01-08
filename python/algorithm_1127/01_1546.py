# https://www.acmicpc.net/problem/1546
import sys

N = int(sys.stdin.readline()) # 몇개의 점수를 받는지, 
scores = [int(i) for i in sys.stdin.readline().split()]
max_score = max(scores)
# 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
new_scores = [i/max_score*100 for i in scores]
avg = sum(new_scores)/N
print(avg)
    

