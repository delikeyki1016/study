# k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    new_word = ""
    # n을 k진수로 변환하기
    while n: # n>0
        new_word = str(n % k) + new_word
        n = n // k
    print(f"진수로 변환된 값은 {new_word}")
    # 변환된 값을 0을 기준으로 나누어 숫자형으로 바꾸어 리스트에 담음 
    new_nums = [int(i) for i in new_word.split("0") if i != '']
    print(f"체크해야할 숫자 리스트 : {new_nums}")
    for i in new_nums:
        is_prime = True
        if i < 2:            
            continue
        for j in range(2, int(i**0.5)+1): 
            # 16을 소수인지 판별하려면, 1~15까지 나눠봐야하지만, 
            # 16의 루트인 값(i**0.5)을 구해서 그 수+1까지만(딱 나누어떨어지지 않을 수 있으므로) 나누면 약수여부를 알 수있다. 
            if i % j == 0:
                is_prime = False
                print(f"{i}는 소수가 아니네요 {is_prime}")
                break
        if is_prime:
            answer += 1    
    return answer

print(solution(8, 2))