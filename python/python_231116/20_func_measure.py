import time

start = time.time()

list = [7,5,9,0,3,1,6,2,4,8]
# for i in range(1, len(list)):
#     key = list[i]
#     j = i - 1
#     while j >= 0 and list[j] > key:
#         list[j + 1] = list[j]
#         j -= 1
#     list[j + 1] = key

# 이중for문 0.001초, 위에 것은 0초 걸림 
for i in range(1, len(list)):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break
print(list)

end = time.time()
print("{0:0.20} sec.".format(end -start))