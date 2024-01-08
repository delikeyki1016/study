# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices) -> str:
    answer = ""
    score_dict = {} # 필요하면 개선
    for i, v in enumerate(survey):
        score_dict[v[0]] = 0 
        score_dict[v[1]] = 0 
    
    for i, v in enumerate(survey):  
        score = choices[i]
        # 점수가 1보다 크거나 같고 3보다 작거나 같으면 앞에 문자를 키로 점수 저장
        if 1 <= score <= 3:
            score_dict[v[0]] += 4 - score
        # 점수가 5보다 크거나 같고 7보다 작거나 같으면 뒤에 문자를 키로 점수 저장
        elif 5 <= score <= 7:
            score_dict[v[1]] += score - 4
            
    
    print(answer)
    
    
    
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])) # "TCMA"