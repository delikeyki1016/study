# import sys
# a, b, c = [int(i) for i in sys.stdin.readline().split()]
# price = 0
# if a == b and b == c and c == a:
#     price = a * 1000 + 10000
# elif a == b or b == c:
#     price = b * 100 + 1000
# elif a == c:
#     price = c * 100 + 1000
# elif a != b and b != c and c != a:
#     price = max(a,b,c) * 100
    
# print(price)

# dict 
import sys

dice_list = [int(i) for i in sys.stdin.readline().split()]
my_dict = {}
for i in dice_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
price = 0
for i in my_dict:
    if my_dict[i] == 3:
        price = i * 1000 + 10000
        break
    elif my_dict[i] == 2:
        price = i * 100 + 1000
        break
    else:
        price = max(my_dict.keys()) * 100

print(price)




