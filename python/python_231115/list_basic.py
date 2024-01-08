alphabet = ['a', 'b', 'c', 'd', 'e']

vow = [alphabet[0], alphabet[4]] # 인덱싱은 요소를 반환함
vow = alphabet[0:5:4] #슬라이싱 0부터5까지 4번을 건너띔 [시작인덱스:전체갯수:스텝] => 슬라이싱은 리스트로 반환함 
consonant = alphabet[1:4]
# print(vow) # a,e
# print(consonant) # b,c,d

new_alphabet = [vow, consonant]
# print(new_alphabet)
# print(new_alphabet[0][1])

alphabet[1] = 3.14
# print(alphabet)

alphabet[0] = [1,2] #요소에 값 자체에 배열[1,2]가 들어감 
alphabet[2:3] = [4,8] # 요소에 추가하려면 슬라이싱으로 넣어야 한다. index2에 4가 되고 8이 추가된다.
# print(alphabet)
num = [1,2,3,4,5]
num.reverse()
print(num) #[5, 4, 3, 2, 1]
# reversed(num) 
# print(num) #[5, 4, 3, 2, 1]