# https://www.acmicpc.net/problem/1541
import sys
expr = sys.stdin.readline().rstrip().split('-')
min_result = 0

print(expr)
for i in expr[0:1]:
    for j in i.split('+'):
        min_result += int(j)

for i in expr[1:]:
    for j in i.split('+'):
        min_result -= int(j)
        print(min_result)
        
print(min_result)
        