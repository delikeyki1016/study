#N개의 수를 입력받아 최대값과 그 인덱스를 출력 
nums = [int(i) for i in input().split()]
# # print(max(nums), nums.index(max(nums)))

max_num = nums[0]
index = 0

for i in range(len(nums)):
    if max_num < nums[i] :
        max_num = nums[i]
        index = i + 1
print("최대", max_num, "index", index)

