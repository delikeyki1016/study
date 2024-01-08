import sys

while True:
    try:
        A, B = sys.stdin.readline().split()
        print(int(A) + int(B))
    except:
        break

        