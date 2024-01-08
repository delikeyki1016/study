import sys
N = int(sys.stdin.readline())
# result = []
# for _ in range(N):
#     age, name = sys.stdin.readline().split()
#     result.append([age, name])
result = [sys.stdin.readline().split() for _ in range(N)]
result.sort(key=lambda x:int(x[0]))
for i in result:
    print(*i)
    
    
    
    
    