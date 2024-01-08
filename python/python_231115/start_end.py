# 리스트의 첫번째 마지막을 더하기 
# 방법1
# nums = input().split()
# start, *_, end = nums
# print(int(start) + int(end))

# 방법2
# nums = [int(i) for i in input().split()]
# print(nums[0] + nums[-1])

# 방법3 
# nums = [int(i) for i in input().split()]
# print(nums.pop(0) + nums.pop())


# 공바꾸기 : 바구니를 총 N개 가지고 있고, 바구니에는 1번부터 N번까지 번호가 매겨져 있다.  

basket, change = [int(i) for i in input().split()] # basket 바구니수, change 바꿀 횟수
ball = [i for i in range(1, basket+1)] # 바구니 리스트
print(ball)
for i in range(change):
    ln, rn = [int(i)-1 for i in input().split()]
    
    ball[ln], ball[rn] = ball[rn], ball[ln]
    
print(ball)





# 공 바꾸기 정답
# N, M  = [int(i) for i in input().split()]
# balls =[i for i in range(1, N+1)]

# for i in range(M):
#     lt, rt = [int(i) - 1 for i in input().split()]
#     balls[lt], balls[rt] = balls[rt], balls[lt]

# print(*balls)