# data = '990209-1******'
# '남자' 또는 '여자'를 리턴
def gender(data):
    gender_num = int(data[7])
    if gender_num % 2 == 1:
        return '남자'
    else :
        return '여자'

# year, month, day 리턴
def birth(data):
    gender_num = int(data[7])
    if  gender_num in [1,2,5,6]:
        year = '19' + data[:2]
    else:
        year = '20' + data[:2]
    month = data[2:4]
    day = data[4:6]
    return int(year), int(month), int(day)

# 6자리-7자리
def hidden_data(data):
    import re
    # if len(data) == 14 and data[:6].isdigit() and data[7:].isdigit():
    # data = data[:6] + "-" + data[6] + ("*" * 6)
    # 정규표현식으로 변경하면, 
    if len(data) == 14 and re.match('^\d{6}-\d{7}$', data):
        data = data[:8] + ("*" * 6) #880101-1******
        return data
    else :
        raise Exception("주민번호 형식이 잘못되었습니다.")
        

if __name__ == "__main__": # 해당 파일을 직접 실행하다면 아래를 실행, 그것이 아니라, 다른 프로그램의 import로서 사용한다면 실행하지마 
    try:
        data = input("주민번호를 입력하세요").replace(" ", "-")
        print(hidden_data(data))
        print(gender(data))   
        print(birth(data))
    except Exception as e:
        print(e)