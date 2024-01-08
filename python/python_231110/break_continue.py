for i in range(1,10) :
    if i == 5 :
        # for문을 아예 빠져나옴
        break 
    print(i)
print('end')

for i in range(1,10) :
    if i == 5 :
        # 아래행을 실행하지 않고 반복을 다시 진행(위로 올라감)
        continue
    print(i)
print('end')
