# 애너그램 체크 
CASE_NUM = int(input()) # 몇번 체크할 것인지,

for _ in range(CASE_NUM) :
    str1, str2 = input().split()

    if sorted(str1) == sorted(str2) :
        print(f'{str1} & {str2} are anagrams.')
        # print("{} & {} are anagrams.".format(word1, word2))
        # print("%s & %s are anagrams." % (str1, str2))
    else :
        print(f'{str1} & {str2} are NOT anagrams.')