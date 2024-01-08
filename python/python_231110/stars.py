# 별찍기
star = int(input())
# j = -1
# for i in range(1, star*2) :
#     if i > star : 
#         j -= 2
#         print(' ' * (i-star) + '*' * j)
#     else : 
#         j += 2
#         print(' ' * (star-i) + '*' * j)
        
    
# 별 찍기 _ for

#    *       # " " : 4, s : 1 (1)
#   ***      # " " : 3, s : 3 (2)
#  *****     # " " : 2, s : 5 (3)
# *******    # " " : 1, s : 7 (4)
#*********   # " " : 0, s : 9 (5)
for i in range(1, star + 1):
    print(" " * (star - i) + "*" * (2 * i - 1))

# *******    # " " : 1, s : 7 (1) (5 * 2 - 1) + (-2 * 1) = 7
#  *****     # " " : 2, s : 5 (2) (5 * 2 - 1) + (-2 * 2) = 5
#   ***      # " " : 3, s : 3 (3) (5 * 2 - 1) + (-2 * 3) = 3
#    *       # " " : 4, s : 1 (4) (5 * 2 - 1) + (-2 * 4) = 1
for i in range(1, star):
    print(" " * i + "*" * ((2 * star - 1) - 2 * i))

# 샘꺼 while 문으로
# i = 1 
# while i < star + 1 :
#     print(" " * (star - i) + "*" * (2 * i -1))
#     i += 1
    
# i = 1  
# while i < star :
#     print(" " * i + "*" * ((star * 2 - 1) + (-2 * i)))
#     i += 1
    
    