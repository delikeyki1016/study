
# 리스트를 문자열로 
# a = ['Life', 'is', 'too', 'short']
# result = " ".join(a)
# print(result)


# # 딕셔너리의 유효한 키값
# a = dict()
# a[('b',)] = 'python'
# a[1] = 'python'
# #a[[1]] = 'python' 리스트는 변경가능한 것이므로 키로 올수없음
# print(a[('b',)])


# 리스트에서 중복제거 
# a = [8,8,8,7,7,7,1,1,1,2,3,3,4,4,5,5,6,7]
# # a = ['a','b','d','c']
# print(a)
# aSet = set(a)
# print(aSet)
# b = list(aSet)
# print(b)

# 파이썬 변수
# a = b = [1,2,3]
# a[1] = 4
# print(b) #[1,4,3]

with open("./book_quiz/복습.txt","w") as f:
    f.write("python hello \n")
    f.write("python is hoo~~~ \n")
    f.write("python! I did it!! \n")


with open("./book_quiz/복습.txt","r") as f:
    for i in f:
        print(i)
