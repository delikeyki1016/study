import sys

try:
    num = int(sys.stdin.readline())
    print(100/num)
except Exception as e:
    # print(f'{num} 으로는 나눌수가 없습니다.')  # 자바스크립트의 try catch와 같다.
    print(e)
    print(e.__class__)
    
print('프로그램이 정상적으로 종료되었습니다.')