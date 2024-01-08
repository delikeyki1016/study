# 순열 개수 리턴하기
import itertools

data = [1, 2, 3]
result = [list(i) for i in itertools.permutations(data)]
print(result)