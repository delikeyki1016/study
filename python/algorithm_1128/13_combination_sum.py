import sys, itertools

# candidates = [int(i) for i in sys.stdin.readline().split()] # [2,3,6,7]
# target = int(sys.stdin.readline()) # 7
# [ [7], [2,2,3] ]

candidates = [2,3,6,7]
target = 7

print([list(i) for i in itertools.combinations(range(1, len(candidates)+1), target)])