import random
import sys

# 랜덤숫자 입력하는 파일 생성
with open('rand_num.txt', 'w') as f:
    for i in range(10):
        f.write(f'{random.randint(1, 20)}\n')
        
# 사용자의 입력을 받아
num = int(sys.stdin.readline())
# 파일을 읽어와서 존재하면 해당 라인번호를 출력, 없다면 -1 
def find_num(num):
    with open('rand_num.txt', 'r') as f:
        # line_num = 0
        for i,v in enumerate(f):
            # print(i)
            # line_num += 1
            # print(type(v))
            if num == int(v):
                return i
        return -1

print(find_num(num))