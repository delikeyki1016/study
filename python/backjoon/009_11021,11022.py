import sys

T = int(sys.stdin.readline())

# for i in range(T):
#     A, B = sys.stdin.readline().split()
#     print(f"Case #{i+1}: {int(A) + int(B)}")

for i in range(T):
    A, B = sys.stdin.readline().split()
    print(f"Case #{i+1}: {A} + {B} = {int(A) + int(B)}")