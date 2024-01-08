import sys

while True:
    A, B = sys.stdin.readline().split()
    if int(A) == 0 and int(B) == 0:
        break
    else:
        print(int(A) + int(B))

