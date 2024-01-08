from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    park_info = defaultdict(list)
    pay_info = defaultdict(int)
    for i in records:
        time, car_num, status = i.split()
        h, m = [int(i) for i in time.split(":")]
        minute = h * 60 + m 
        park_info[car_num].append(minute)
    
    for key,v in park_info.items():
        if len(v)%2 == 1:
            v.append(23 * 60 + 59)    
        pay = v[1] - v[0]
        if len(v) > 2:
            pay += (v[3] - v[2])
        if pay <= fees[0]:
            pay = fees[1]
        else:
            pay = fees[1] + (math.ceil((pay - fees[0]) / fees[2]) * fees[3])
        pay_info[int(key)] = pay
    
    pay_info = sorted(pay_info.items())
    for i in pay_info:
        answer.append(i[1])
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))