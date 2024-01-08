# 제너레이터는
# 1.
# def get_natural_num():
#     n = 0
#     while True:
#         n += 1
#         yield n # n 반환
        
# n_num_generator = get_natural_num()

# print(n_num_generator) # <generator object get_natural_num at 0x000001F97A494B80> 할당된 주소가 나옴 
# print(n_num_generator) # <generator object get_natural_num at 0x000001F97A494B80> 할당된 주소가 나옴 
# print(n_num_generator) # <generator object get_natural_num at 0x000001F97A494B80> 할당된 주소가 나옴 

# for i in range(100): # range가 대표적인 제너레이터이기 때문에 아래 next는 필요가 없음 
#     print(next(n_num_generator))



# 2.
# def get_many_type_data():
#     while True:
#         yield 1
#         yield '문자열'
#         yield True
        
# n_num_generator = get_many_type_data()

# print(n_num_generator) # <generator object get_many_type_data at 0x0000021DA8FD49E0>
# print(n_num_generator)
# print(n_num_generator)

# for i in range(10): 
#     print(next(n_num_generator))



# 3.
# a = [i for i in range(10000)]
# b = range(10000)

# print(len(a)) # 10000
# print(len(b)) # 10000

import sys
# print(sys.getsizeof(a)) # 85176 (메모리사이즈)
# print(sys.getsizeof(b)) # 48     (메모리사이즈)



# 4. enumerate 낱낱이 세다
rainbow = ['빨','주','노','초','파','남','보']

# enum_rainbow = enumerate(rainbow)

# print(enum_rainbow)
# print(list(enum_rainbow))

for index, color in enumerate(rainbow):
    print(index, color)



# 5. locals()
import sys # 시간초과 이슈가 있어요!!!

s = set()
calc_count = 5
cmd = ["add 1", "check 1", "check 2", "all", "toggle 1"]
for i in cmd:
    command = i.split()
    if command[0] == 'add':
        num = int(command[1])
        s.add(num)
    elif command[0] == 'remove':
        num = int(command[1])
        s.discard(num)
    elif command[0] == 'check':
        num = int(command[1])
        if num in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        num = int(command[1])
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif command[0] == 'all':
        s = set([i for i in range(1, 20 + 1)])
    elif command[0] == 'empty':
        s = set()

# print(locals()) 내부의 모든 로컬변수를 출력해준다. 디버깅에 유용 

# # import pprint
# # pprint.pprint(locals())

from pprint import pprint
pprint(locals())