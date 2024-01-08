from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        course_size_list = []
        for j in orders:
            course_size_list.extend(list(combinations(sorted(j), i)))
        most_common = Counter(course_size_list).most_common()        
        for i, v in most_common:
            if v >= 2 and v == most_common[0][1]:
                answer.append(''.join(list(i)))
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
# 	["ACD", "AD", "ADE", "CD", "XYZ"]

print(solution(orders, course))