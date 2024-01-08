import sys

T = int(sys.stdin.readline())
for _ in range(T):
    R, S = sys.stdin.readline().split()
    result = ''
    for i in range(len(S)):
        result += S[i]*int(R)
    print(result)
        
        

