import sys 
def hundred_divisor():
    try:
        print("100의 약수를 입력하세요")
        num = int(sys.stdin.readline().rstrip())
        if 100 % num == 0:
            print("약수입니다.")
        else :
            print("틀렸습니다.")
    except ZeroDivisionError as e :
        print("0으로 나눌수는 없어요", e)
        hundred_divisor()
    except ValueError as e:
        print("정수값을 입력하지 않아 프로그램을 종료합니다.", e)
    except KeyboardInterrupt as e:
        print("키보드 입력으로 강제 종료하였습니다.", e)
    except Exception as e: # 마지막에 포괄적으로 넣어주는 에러메시지이므로, 가장 최상위 에러를 써준다.
        print("알수 없는 에러", e)
    else: # except가 발생되면 실행되지 않음. except가 없을 경우 실행됨, (선택사항) 
        print("예외없이 잘 처리되었습니다.")
    finally : # except 여부와 상관없이 무조건 실행 (선택사항) 
        print("프로그램이 종료되었습니다.")
        
hundred_divisor()
    