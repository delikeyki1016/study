# 예외 형식 만들기 
class MyException(Exception):
    # Exception을 상속받음
    def __init__(self):
        super().__init__(self, '예상치 못한 답변으로 에러가 발생함')

select = int(input("파이썬이 좋으면 1번, 아니면 2번"))
try:
    if select == 1:
        print('역시 파이썬은 좋아요')
    elif select == 2:
        raise MyException()
    else:
        print('1번 또는 2번을 입력하세요.')
except Exception as e:
    print(e)  
    
# a = MyException()
# print(a)