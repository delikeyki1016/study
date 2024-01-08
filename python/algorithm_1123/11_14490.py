def baek_dae_yeol(n, m):

    # 최대공약수(greatest_common_divisor) 구하기
    # def gcd(a, b):
    #     # if a < b:
    #     #     a,b = b,a 
    #     while b != 0:
    #         a, b = b, a%b
    #     return a  # 최대공약수 
    
    # n_m_gcd = gcd(n,m)
    # print(f'{n//n_m_gcd}:{m//n_m_gcd}')
    
    
    # 숙제 : 최대공약수를 안구하고 짜보기 (재귀)
    #A, B를 나눈 나머지가 (A % B) = 0이 될 때까지 (B, A % B)를 계산
    
    def measure(a, b):
        if a % b == 0:
            return b
        return measure(b, a%b) 
    
    n_m_gcd = measure(n,m)
    print(f'{n//n_m_gcd}:{m//n_m_gcd}')
    
    
    # 숙제 : 최대공약수를 안구하고 짜보기
    
    # # 약수를 구하는 함수
    # def measure(num):
    #     num_list = []
    #     for i in range(2, num+1):
    #         if num % i == 0:
    #             num_list.append(i)
    #     return num_list

    # n_list = measure(n)
    # m_list = measure(m)

    # # 두 리스트 중 최대약수가 작은 것을 선택
    # if n_list[-1] > m_list[-1]:
    #     min_list = m_list
    #     max_list = n_list
    # else:
    #     min_list = n_list
    #     max_list = m_list
    
    # # 작은 리스트 요소 중에서 큰 리스트에 있는 요소 중 최대값을 선택 
    # n_m_gcd = 1   
    # for i in min_list:
    #     if i in max_list:
    #         n_m_gcd = i
    
    # print(f'{n//n_m_gcd}:{m//n_m_gcd}')

import sys
n, m = [int(i) for i in sys.stdin.readline().split(":")]
baek_dae_yeol(n, m)