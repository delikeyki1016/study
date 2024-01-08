import itertools

nums = [1, 2, 3]
result = []

for i in range(len(nums)+1):
    for j in itertools.combinations(nums, i):
        result.append(list(j))
# result = [list(j) for i in range(len(nums)+1) for j in itertools.combinations(nums, i)]

print(result)