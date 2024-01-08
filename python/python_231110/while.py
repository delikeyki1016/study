# 1~30 사이의 무작위 수를 뽑아 정답 맞추기

import random

random_num = random.randint(1, 30) #1,30 포함
# print(random_num)

while True :
    user_input = int(input('1~30 사이의 숫자를 입력하세요.\n'))
    
    if user_input == random_num :
        print("정답")
        break
    elif user_input < random_num :
        print("Up")
    else :
        print("Down")