def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))