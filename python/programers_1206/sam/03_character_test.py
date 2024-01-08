# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict

def solution(survey, choices) -> str:
    """
        질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와
        검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어지고,
        검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하는 함수
    Args:
        survey (list): "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나
            성격유형 검사 문항으로 두 성격을 대표하는 알파벳 대문자로 구성되어있다.
        choices (list): 각 문항에 대한 결과점수
            1. 앞 알파벳 성격 3점
            2. 앞 알파벳 성격 2점
            3. 앞 알파벳 성격 1점
            4. 0점
            5. 뒤 알파벳 성격 1점
            6. 뒤 알파벳 성격 2점
            7. 뒤 알파벳 성격 3점

    Returns:
        str: 검사결과로 성격 알파벳 반환 (동일한 점수면 사전식이 우선)
    """
    answer = ""
    score_dict = defaultdict(int)
    for i, v in enumerate(survey):  
        score = choices[i]
        # 점수가 1보다 크거나 같고 3보다 작거나 같으면 앞에 문자를 키로 점수 저장
        if 1 <= score <= 3:
            score_dict[v[0]] += 4 - score
        # 점수가 5보다 크거나 같고 7보다 작거나 같으면 뒤에 문자를 키로 점수 저장
        elif 5 <= score <= 7:
            score_dict[v[1]] += score - 4
    
    character_info = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for i in character_info:
        if score_dict[i[0]] >= score_dict[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
            
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])) # "TCMA"