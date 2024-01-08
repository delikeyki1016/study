import sys
words = (sys.stdin.readline().rstrip()).upper()
unique_words = list(set(words)) # 중복허용없는 set사용 후 인덱스를 갖는 리스트로
cnt_list = []
for i in unique_words:
    cnt_list.append(words.count(i)) # 해당 단어의 갯수를 세어 리스트에 담기

if cnt_list.count(max(cnt_list)) > 1: # 갯수가 가장 큰 값의 개수가 1개 이상이면 ? 출력
    print('?')
else:
    print(unique_words[cnt_list.index(max(cnt_list))]) # 갯수가 가장큰값의 인덱스로 해당 워드 출력