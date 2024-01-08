# N, X = [int(i) for i in input().split()]
# A = set()
# for _ in range(N):
#     num = int(input())
#     if num < X:
#         A.add(num)

# print(*A)


# A의 요소에서 X보다 작은 수만 출력 
X = int(input())
A = [int(i) for i in input().split()]

result = []
for i in A :
    # print(result) # del을 쓰면 A리스트에서 값이 지워졌기 때문에, range 범위를 벗어나게 된다. 반복문이 동작하면서 배열의 크기가 변경되면 정상적인 반복이 불가능할 수 있다. 따라서 del은 쓰지 말자
    if i < X :
        result.append(i)

print(result)


# 샘코드
# X 보다 작은 수
# N, X = [int(i) for i in input().split()]
# A = [int(i) for i in input().split()]

# # A 안에서 X보다 작은 수를 결과물로 출력
# result = [i for i in A if i < X]
# # spread operator인 *을 사용하면,
# # 리스트의 요소를 unpacking해서 출력할 수 있습니다.
# print(*result)