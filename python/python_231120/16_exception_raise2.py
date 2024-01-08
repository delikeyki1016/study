# 홀수만 더해서 출력
def sum_odd_to_ten():
    try:
        number = get_number()
        print(number)
        sum = 0
        range_number = number + 1
        # if number % 2 == 1:
        #     range_number += 1
        for i in range(1, range_number, 2):
            sum += i
        print(f'1) 1부터 {number}까지 홀수의 합은{sum} 입니다.')
    except Exception as err:
        print(err)
        raise Exception("2) 에러를 전달합니다.") # 27줄에 err에 메시지를 전달한다.
            
            
def get_number():
    number = int(input("숫자를 입력하세요"))
    if number < 1:
        raise Exception("1) 예외가 발생했습니다. 자연수만 입력할 수 있습니다.") # sum_odd_to_ten() 14줄로 이동해서 err에 메시지를 전달한다.
    return number

try:
    sum_odd_to_ten()
except Exception as err:
    print(err)