strs = ['하마야', '하마', '하늘아래', '하데스', '하늘', '하수구']
strs.sort(key=lambda x:(len(x), x)) # 글자길이 순서, ㄱㄴㄷ
print(strs)