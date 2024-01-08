from collections import deque
def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    answer = 0
    
    # 내부에서 합계를 구하면 시간 초과
    sum1 = sum(deque1)
    sum2 = sum(deque2)    
    
    # 두 큐의 합계를 구했을 때, 큰 큐에 있는 것을 작은 큐에 붙여주는 형태로 반복
    while True:
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            i = deque1.popleft()
            deque2.append(i)
            sum1 -= i
            sum2 += i
            answer += 1
        elif sum1 < sum2:
            i = deque2.popleft()
            deque1.append(i)
            sum2 -= i
            sum1 += i
            answer += 1
        if len(deque1) == 0 or len(deque2) == 0 or answer == (len(deque1) + len(deque1)) * 2:
            return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))