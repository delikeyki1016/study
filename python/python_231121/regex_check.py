import re

def match_check(regex, string):
    if re.search(re.compile(regex), string):  # regex를 컴파일한 객체가 string에서 찾아지면 아래 수행, re.compile(regex), string  => regex, string (동일)
        # print(f'{regex}, {string} is match!')
        print("T")
    else:
        # print(f'{regex}, {string} is ' + '\033[101m' + 'Not' + '\033[0m' + ' match!')
        print("F")
