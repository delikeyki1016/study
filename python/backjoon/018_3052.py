import sys
remain = []
for _ in range(10):
    num = int(sys.stdin.readline())
    temp = num % 42
    if temp not in remain:
        remain.append(temp)
print(len(remain))
    