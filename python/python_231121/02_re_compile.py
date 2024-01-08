import re

# c_obj = re.compile(r'[a-z]+')
# match_obj = c_obj.match('pyth0n')
# 축약
# match_obj = re.match('[a-z]+', 'pyth0n') 

match_obj = re.search('[a-z]+', 'pyth0n') # 문자열 전체(끝까지)를 확인함

print(match_obj.group()) # pyth, ()묶음 단위 출력인데, 여기서는 첫번째만 출력되네? 
print(match_obj.start()) # 0, 시작단어 index 출력 
print(match_obj.end())   # 4, 오류나는 첫단어 index 출력 
print(match_obj.span())  # (0, 4) 시작index 끝index 묶어서 출력 

# match_obj = re.findall('[a-z]+', 'pyth0n') #매치된 문자열을 리스트로 반환해줌 ['pyth', 'n']

# match_obj = re.finditer('[a-z]+', 'pyth0n') #매치된 결과를 반복 가능한 객체로 반환해줌

# print(match_obj)
# for i in match_obj:
#     print(i.group()) #pyth, n 



# re.sub(패턴, 대체문자, 대상문자)
target = 'aabaaabcca'
target = re.sub('[a]+',"안녕", target) # a가 한번이상 반복되면 안녕으로 대체해라 

print(target)