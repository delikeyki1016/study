# k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    new_word = ""
    # n을 k진수로 변환하기
    while n:
        new_word = str(n % k) + new_word
        n = n // k
    # print(f"진수로 변환된 값은 {new_word}")
    new_nums = [int(i) for i in new_word.split("0") if i != '']
    # print(f"체크해야할 숫자 리스트 : {new_nums}")
    for i in new_nums:
        is_prime = True
        if i < 2:
            continue
        # 2부터 제곱근의 정수까지 나누었을 때, 나머지가 0이 아니면 소수다!!!
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                # print(f"{i}는 소수가 아니네요")
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer

print(solution(80709018, 10))