def number_to_words(num: int) -> str:
    nums_dict = {
        100_000_000 : '억', 10_000 : '만', 1_000: '천', 100 : '백', 10 : '십',
        9: '구', 8: '팔', 7: '칠', 6: '육', 5: '오', 4: '사', 3: '삼', 2: '이', 1: '일'
    }
    if num == 0:
        return '영'
    result = ""
    # 1) nums_dict에서 키와 값을 가져와는 형태로 반복문 실행 (키: key, 값: kor)
    for key, kor in nums_dict.items():
        # 2) 만약 num가 key보다 크거나 같으면,
        if num >= key:
            # 3) num에서 key를 나눈 몫을 count
            count = num // key
            # 4) num에서 key를 나눈 나머지를 num
            num %= key
            # 5) 만약에 몫이 1보다 크면
            if count > 1:
                # 6) result += 몫을 매개변수로 재귀 호출 진행(count) + kor
                result += number_to_words(count) + kor
            else:
            #   7) 해당 단어(kor)를 붙인다.
                result += kor
    return result
        
print(number_to_words(1234))