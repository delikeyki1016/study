N = 4
k = 2

# 서로 다른 N개에서 순서에 상관없이 K개를 선택하라
result = []
def combine(k, start, list = []):
    if k == 0:
        result.append(list[:]) # 중요
        return
    for i in range(start, N+1):
        list.append(i)
        combine(k - 1, i + 1, list) # 중요
        list.pop() # 중요
combine(k, 1)
print(result)

# 리스트 = []
# 1부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
# 1. [1]
#       2부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#       1. [1] + [2]
#               3부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
#       2. [1] + [3]
#               4부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
#       3. [1] + [4]
#               4+1부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
# 2. [2]
#       3부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#       1. [2] + [3]
#               4부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
#       2. [2] + [4]
#               4+1부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
# 3. [3]
#       4부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#       1. [3] + [4]
#               4부터 4+1까지 데이터를 반복합니다. 그래서 리스트에 추가합니다
#               !!!!!!! 추가안해요~ 왜? 리스트의 길이가 K와 동일해졌으니! 그만~~~
# 4. [4]
#       ~
