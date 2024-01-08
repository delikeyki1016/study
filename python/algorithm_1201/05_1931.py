# https://www.acmicpc.net/problem/1931
import sys

N = int(sys.stdin.readline())

meeting = []
for _ in range(N):
    start, end = [int(i) for i in sys.stdin.readline().split()]
    meeting.append((start, end))

meeting = [(12, 14), (2, 13), (8, 12), (8, 11), (6, 10), (5, 9), (3, 8), (5, 7), (0, 6), (3, 5), (1, 4)]
meeting.sort(key=lambda x:(x[1], x[0])) # end 가 이른 순으로 정렬, 빨리 끝나는 순으로 정렬해야 다음 팀을 받을 수 있고, 끝나는 시간이 동일하다면, 빨리 시작하는 팀 순으로 정렬
print(meeting)

cnt = 0
finish_time = 0
for i in meeting:
    start_time, end_time = i
    if start_time >= finish_time:
        cnt += 1
        finish_time = end_time
        
print(cnt)