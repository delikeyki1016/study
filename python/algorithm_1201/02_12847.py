# # https://www.acmicpc.net/problem/12847
# import sys

# n, m = [int(i) for i in sys.stdin.readline().split()] # n 일급 개수, m 일하는 가능날
# pay = [int(i) for i in sys.stdin.readline().split()] # 일급 리스트
# window = sum(pay[:m]) # m날까지의 토탈일급
# max_pay = window # 최초 값을 맥스로 정해두고. 
# for i in range(n - m): # 전체 일급에서 window만큼을 뺀 나머지만 반복
#     window += pay[i+m] - pay[i] # 첫 윈도우에서 그 다음값을 더하고 , 앞에 값을 빼줌
#     print('반복', pay[i+m], pay[i], window)
#     max_pay = max(max_pay, window)
    
# print(max_pay)

# while문 적용
import sys
N, m = [int(i) for i in sys.stdin.readline().split()]
pay = [int(i) for i in sys.stdin.readline().split()]

start = 0
window = sum(pay[:m])
max_sum = window

while m < N:
    window += pay[m] - pay[start]
    # print(window)
    max_sum = max(max_sum, window)
    start += 1
    m += 1
print(max_sum)