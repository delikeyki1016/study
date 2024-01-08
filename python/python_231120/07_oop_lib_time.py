import time
# 시간을 초단위(UTC : Univesal Time Coordination 협정 세계시)로 반환
print(time.time()) 

# 연월일시분초 형태로 변환
print(time.localtime()) #tm_wday=0 월요일 , tm_yday=324 324일, tm_isdst=0 썸머타임여부

# 시간을 요일,월,일,시,분,초, 연도 순 의 문자열로 반환 
print(time.asctime())

# sleep 만큼 딜레이
print('10까지 세기')
time.sleep(10)
print('지금') # 10초 후 프린트
