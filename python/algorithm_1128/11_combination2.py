import itertools
N = 4
K = 2

print([list(i) for i in itertools.combinations(range(1, N+1), K)])