# 문자열을 한자리씩 더해서 출력
import sys

su = int(sys.stdin.readline())
nums = sys.stdin.readline().rstrip() # readline()은 엔터를 포함하기 때문에 뒤의 엔터를 삭제해야함 

sum = 0
for i in nums:
    sum += int(i)
    
print(sum)