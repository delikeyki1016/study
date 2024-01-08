# 파일 생성 후 쓰기
# f = open("python_231117/test.txt", "w", encoding='utf-8') # 일반적으로 f로 사용 
# for i in range(1, 5+1):
#     data = f'안녕 파이썬{i}! \n'
#     f.write(data)
# f.close()

# 파일 읽기
# f = open("python_231117/test.txt", "r") 
# while True:
#     line = f.readline()
#     # readline은 더 이상 읽을 라인이 없는 경우, None을 출력한다.
#     # 그래서 무한루프가 여기서 빠져나올 수 있다.
#     if not line:
#         break
#     print(line.rstrip())
# f.close()

# 파일 전체 읽기
# read 함수는 파일을 한 번에 읽어서 모두 가져온다.
# 만약에 파일의 크기가 크다면, 메모리의 사용이 커진다!
# data = f.read()

# 파일 순회
# f = open('python_231117/test.txt', 'r', encoding='utf-8')
# # f 는 파일의 순회가 가능한 객체(iterable)!
# for line in f:
#     print(line.rstrip())
# f.close()

# 파일 내용 추가
# f = open("python_231117/test.txt", "a", encoding = 'utf-8') 
# for i in range(6, 10+1):
#     data = f'hello {i}! \n'
#     f.write(data)
# f.close()

# with open() as f: 는 open, close 가 동작함 
with open("with.txt", 'a', encoding='utf-8') as f:
    f.write("with 블록을 벗어나는 순간, 파일 객체 f가 자동으로 close 됩니다.")
    
