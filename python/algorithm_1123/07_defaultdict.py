import collections

# 에러
# my_dict = {}
# print(my_dict['a'])

# my_dict = collections.defaultdict(int) # 키가 없어도 자동으로 키값을 생성해준다. 
# print(my_dict['a'])

my_dict = collections.defaultdict(int)
my_dict['first'] = 5
my_dict['second'] = 4
print(my_dict['first'], my_dict['second'], my_dict['third'])