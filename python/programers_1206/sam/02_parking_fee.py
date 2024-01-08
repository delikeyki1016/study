import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    park_info = defaultdict(list)
    for i in records:
        time, car_num, status = i.split()
        h, m = [int(j) for j in time.split(":")]
        minute = h * 60 + m
        park_info[car_num].append(minute)
    
    park_fee = defaultdict(int)
    for k, v in park_info.items():
        if len(v) % 2 == 1:
            v.append(23 * 60 + 59)
        park_time = 0
        for i, m in enumerate(v):
            if i % 2 == 0:
                park_time += v[i+1] - v[i]
        park_fee[k] = park_time
        # park_fee[k] = sum([v[i+1] - v[i] for i in range(len(v)) if i % 2 == 0])
        
    answer = sorted(park_fee.items())
    for i in range(len(answer)):
        if answer[i][1] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + (math.ceil((answer[i][1]-fees[0])/fees[2]) * fees[3])
    return answer

fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT"
    ]

print(solution(fees, records)) # [14600, 34400, 5000]