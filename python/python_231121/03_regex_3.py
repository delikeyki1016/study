import re
match_obj = re.search('(\w+)\s+([0,1]{3}[-]\d{4}[-]\d{4})', '홍길동 010-1234-5678')

print(match_obj)

print('그룹0',match_obj.group(0)) # 매칭된 문자열 전체 출력
print('그룹1',match_obj.group(1)) # 1그룹 출력
print('그룹2',match_obj.group(2)) # 2그룹 출력

# 

pattern_dict = {
    'mobile': '^(01[0|1|6|7|8|9])-(\d{3,4})-(\d{4})$', #()그룹으로 묶는 건 선택사항 
    'email' : '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', # (대소문자,숫자, ._%+-)@().()
    'ipv4' : '^[0-9]{1,3}[.][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$',  # '^([0-9]{1,3}[.]){3}[0-9]{1,3}$'
                                                                # 127.0.0.1 => 255.255.255.255 각 숫자의 최대숫자 (:80번이 기본값, 자물쇠(https)일때 443)
    'url': '^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', #http, https://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
    'date': '^\d{4}-\d{2}-\d{2}$', # 2023-11-21  '^\d{4}-[0-1]\d-[0-3]\d$'
    'time': '^[0-9]{2}:[0-9]{2}:[0-9]{2}$', # 13:02:24
    'password': '^[a-zA-Z0-9!@#$%^&*]{6,30}$' # 대문자 필요,소문자 필요,숫자 필요,특수문자(!@#$%^&*) 필요, 최소 6자리 이상 - 30자 이하
}