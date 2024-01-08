#딕셔너리를 이용한 애너그램 
CASE_NUM = int(input())

for i in range(CASE_NUM):
    word1, word2 = input().split()
    print(word1, word2)
    
    d_word1 = {}
    for i in word1:
        if i in d_word1 :
            d_word1[i] += 1
        else :
            d_word1[i] = 1
    
    d_word2 = {}
    for i in word2:
        if i in d_word2 :
            d_word2[i] += 1
        else :
            d_word2[i] = 1
    print(d_word1, d_word2)
    if d_word1 == d_word2 :
        print(f"{word1} & {word2} are anagrams.")
    else :
        print(f"{word1} & {word2} are NOT anagrams.")