import collections

student_list = ['서유경','정준혁', '서유경', '정준영', '서유경', '정준영']
student_counter = collections.Counter(student_list)

# print(student_counter)
# print(dict(student_counter))

print(student_counter.most_common())
print(student_counter.most_common(1)) # 가장많이 나오는 하나를 가져옴 

# for k, v in student_counter.items():
#     print(k,v)
    
