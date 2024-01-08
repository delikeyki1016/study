import sys

def up_and_down():
    import random
    # 1부터 30까지 무작위로 숫자 선택
    random_num = random.randint(1, 30)

    while True:
        user_input = int(sys.stdin.readline())
        if user_input < 1 or user_input > 30:
            raise ValueError("원하는 숫자의 범위를 초과")
        if user_input == random_num:
            print('정답입니다!!!')
            break # 정답인 경우에 무한반복이 종료!
        elif user_input > random_num:
            print("Down")
        else:
            print("UP")
            
# up_and_down()

try :        
    up_and_down()
except Exception as e:
    print(e)