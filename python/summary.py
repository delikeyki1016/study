# 인터프리터 언어 : 파이썬(실행속도가 느리다), 자바스크립트 한줄씩 순차적 해석, 범용프로그래밍 언어, 간결, 가독성 좋다. 타 언어와의 호환성 좋다.
# 설치 https://www.python.org/downloads/ : 설치 시 path 추가를 선택해야함 
# cmd - python 입력, 나가기 exit() or ctrl+z
# cmd - code . ==> 현재폴더를 VScode로 열어줌 

# 들여쓰기 필수 
# 네이밍컨벤션(PEP8) : 소문자 + _ (스네이크 케이스)
# 첫글자가 알파벳 또는 _ 가능 ex) ____ab 가능
# integer : 정수 123, -123, 0 / float : 실수 0.1 / string : 문자나열 / complex : 복소수,허수 2+3j 
# 제곱 : a = 3, b = 4, a ** b => 3의 4제곱 = 81  (제곱이 연산 우선순위가 높다.0순위)
# 연산에서 float가 섞이면 결과도 float
# 나머지의 몫의 정수만 리턴 7//4 ==> 1 (7/4=1.75)
# 8진수 0o34 (18) / 16진수 0x12 (18) / 2진수 1010 => 10
# 2진수 64 32 16 8 4 2 1
#                1 0 1 0 => 10    
# 변수 : 타입 지정 필요 없음 (동적 타이핑 언어, 값에 따라 타입이 변경)
# 상수는 대문자로
# ''' or """ 여러줄 입력 
# 문자열은 시퀀스 객체이고, 불변객체이다. a = 'aa' , a = 'bb' 재정의하면 a라는 변수는 'bb'의 주소값을 가르킨다. 'aa', 'bb' 는 이뮤터블(불변)
# str[0:3] => index 0 ~ index 2까지  ==> 0 <= str < 3 의 의미 
# str[:5] => str[0:5] 0생략 가능 
# str[5:] => index5~끝까지
# str[-5:] => 뒤에서부터5자리~끝까지
# str[5:8] => index5 ~ index7까지 
# 문자열 formatting : %d (숫자 데이터타입) %s (문자 데이터타입) 
# "name: {0}, age: {1}".format('홍길동', 30) => name: 홍길동, age: 30
# '{0:0.2f}'.format(1.2345) =>1.23
# '{0:5.3}'.format(1.2345) => 1.23 => 총5글자로 세글자만 표기 빈곳은 스페이스 처리됨
# i = 3 일 경우 f'{i} x {i}' => 3 x 3 
# strip() 공백제거 lstrip() rstrip()
# range(start, stop, 증가수) 
# range 함수는 반복 객체(제너레이터)를 반환 => 메모리 소모가 적다.

# python 데이터타입 : Numeric(int, float, complex), Dictionary, bool(0,1로 구성되어있기 때문에 int에 포함됨), Set, Sequence Type(str, list, tuple)


# 리스트
# *을 사용하면, 리스트의 요소를 unpacking해서 출력할 수 있습니다.

# a = ['Life', 'is', 'too', 'short']
# result = " ".join(a)

# 튜플 : 시퀀스(순서) 타입, 소괄호 이용(소괄호 생략가능) , 를 꼭 붙여야 함, 값을 변경할 수 없고, 삭제도 안된다(튜플과 str은 불변, 리스트는 가변)
my_tuple = (1,) # or my_tuple = 1,
print(my_tuple, type(my_tuple)) #(1,) <class 'tuple'>

# 딕셔너리 : 자바스크립트의 Object개념 
# 선언방법
# empty_dict1 = {}
# empty_dict2 = dict()
# 딕셔너리의 key는 변경가능하지 않는 값으로 넣어야 한다. key로는 list가 올 수 없음(list는 가변이므로)

son_dict = {
    'name': '손흥민',
    'age': 29,
    'address': ['대한민국', '영국', '독일']
}

# print(son_dict.keys()) # key만을 모아서 반환
# print(son_dict.values()) # value만을 모아서 반환
# print(son_dict.items()) # key와 value를 튜플로 묶어서 반환

# print(son_dict.get('name')) # 키가 name인 value 반환
# print(son_dict.get('job')) # 키가 job인 value 반환(없어서 None)
# print(son_dict.get('job', '무직')) # 키가 job인 value 반환(없어서 '무직')

for k, v in son_dict.items():
    print(f"Key : {k}, Value: {v}")
    
son_dict.clear()

# 세트 : 집합, 순서가 없고 중복허용하지 않음, 검색의 시간복잡도가 O(1)이다 
# my_set = set() 
# my_set = set([1,2,3,4,5])
# my_set = {}

my_set1 = set([1,2,3,4,5,6])
my_set2 = set([4,5,6,7,8,9])

# 합집합
print(my_set1 | my_set2)
print(my_set1.union(my_set2))

# 교집합
print(my_set1 & my_set2)
print(my_set1.intersection(my_set2))

# 차집합
print(my_set1 - my_set2) #{1, 2, 3}
print(my_set1.difference(my_set2)) #{1, 2, 3}

# 대칭차집합
print(my_set1 ^ my_set2) #{1, 2, 3, 7, 8, 9} 교집합을 뺀 나머지 집합 
print(my_set1.symmetric_difference(my_set2))

num_set1 = set([1, 2, 3])
num_set2 = set([3, 4])

num_set2.add(5) # 요소 추가
num_set1.update(num_set2) # 세트에 다른 세트를 추가 (합집합)  

num_set2.pop() # 첫번째 뽑음
num_set2.remove(5)  # 요소 5를 삭제 

num_set2.clear() # 요소 모두 삭제 

num_set2 = num_set1.copy() # 복제 

# 함수 
# 함수 내의 변수는 항상 함수내 지역변수이다!, 전역으로 사용하려면 global로 선언하거나 전역변수에 담아서 사용해야한다.
# args
def hello2(*names): # 가변매개변수는 맨 앞으로 사용해야함, 두번째 매개변수는 키워드가 꼭 있어야 함, *는 튜플로 받아옴  
    for i in names :
        print(f'Hello {i}')

hello2('kang', 'hong')

# kargs
def hello(**names): # **은 딕셔너리로 받아옴
    for i in names :
        print(f'{i} {names[i]}')
        
hello(kang = 'Hi', 강은영 = '안녕하세요')


# 함수를 변수에 할당하고 사용할 수 있다.
import sys
new_input = sys.stdin.readline 

data = new_input()
print(data)

# import sys
# a, b, c = [int(i) for i in sys.stdin.readline().split()]
# print(a + b + c)

# 클래스는 앞문자를 대문자로
# 클래스는 추상화시킨 것. 구체적 실체는 클래스를 이용해 만든 인스턴스이다. 


# 객체지향 이론 - 캡슐화
# 실제 구현 내용의 일부를 외부에 감추어 은닉하는 것

# 객체지향 이론 - 다형성 => 오버라이딩

# 예외처리
# try:
#   실행할 코드
# except:
#   문제가 생겼을 때 실행할 코드 
# else:
#   except절을 만나지 않았을 때 실행할 코드, except로 들어가면 실행되지 않음, 즉 try가 에러없이 잘 실행된다면 해당else가 실행된다.
# finally:
#   try후에 또는 예외처리 후에 무조건 실행된다. 생략가능 

# raise 는 예외를 발생시켜 상위에 전달함. raise Exception("에러가 발생했습니다.") 일 경우 해당 메시지를 상위의 exception에 전달한다. 

# 정규표현식 : 복잡한 문자열을 처리하는 기법, Reqular Expression, re모듈

# 비선형자료구조 - 이진트리 순회 
# 전위순회 중-왼-오 / 중위순회 왼-중-오 / 후위순회 왼-오-중 => 즉 중간(루트노드)를 중심으로 전,중,후 

# 힙 : 트리 기반의 자료구조, 파이썬에서는 최소힙만 지원

# ==(데이터에 대한 비교), is(메모리에 대한 비교)
arr1 = [1,2,3]
arr2 = arr1 # 같은 주소를 공유함
print(arr1 == arr2) # true
print(arr1 is arr2) # true

arr1 = [1,2,3]
arr2 = arr1[:] # 다른 주소(얇은 복사)
print(arr1 == arr2) # true
print(arr1 is arr2) # false

arr_in = [4,5]
arr1 = [1,2,3, arr_in]
arr2 = arr1[:] # 다른 주소이지만, 참조되는 arr_in은 함께 공유된다.
print(arr1 == arr2) # true
print(arr1 is arr2) # false

arr_in.append(6)
print(arr2) # 6이 포함됨 

# 깊은복사는 아예 다른 객체를 만듦

# 퀵정렬, 병합정렬은 빠르다. 정렬이 되어있는 경우의 퀵정렬은 최악

# O(1) < O(log n) < O(n) < O(n log n) < O(n**2) < O(2**n) < O(n!)

# 투포인터 : 정렬된 리스트에 적합. 투 포인터 기법은 정렬되어 있는 선형 자료구조에서 주로 사용되며, 두 포인터를 사용해 범위를 좁혀가며 문제를 해결 

# 연결리스트가 메모리 효율적

# 해시테이블 : 서로 다른 키를 같은 해시로 돌렸을 때 충돌. 

# DFS(깊이우선탐색) : 스택, 재귀(백트래킹) / BFS(너비우선탐색) : 큐 

# 트리는 그래프의 일종이다.

# 이진트리는 최대 2개의 자식을 갖음 

# 파이썬은 최소힙만 구현 가능

# 안정정렬 : 병합정렬, 불안정정렬 : 퀵정렬

# 병합,퀵의 공통점은 분할정복 

# sort()는 병합과 삽입정렬을 조합한 것 

# 슬라이딩윈도우는 윈도우 크기는 불변하고 위치값이 변경됨 

# 그리디 알고리즘은 근사치를 찾아냄. 각 단계별로 최선의 선택을 할 뿐(근시안적) 무조건 정답을 찾아내는 것은 아니다.

# 다이나믹 프로그래밍은 이미 했던 계산을 저장해서 재활용함으로써 속도 개선

# 객체를 생성할 때 가장 먼저 호출되는 함수, 즉 객체를 생성하면 __init__ 함수가 자동으로 실행되어 생성된다.

# glob # 파일 목록 추출

# shutil # 파일복사