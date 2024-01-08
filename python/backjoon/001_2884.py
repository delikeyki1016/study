# https://www.acmicpc.net/problem/2884

import sys

hour, minute = [int(i) for i in sys.stdin.readline().split()]

pre_minute = minute - 45
if pre_minute < 0:
    hour -= 1
    if hour < 0:
        hour = 24 - 1
    pre_minute = 60 + pre_minute
    
print(hour, pre_minute)