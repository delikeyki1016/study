# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜를 일자로 구하기
    def to_day(date):
        y, m, d = [int(i) for i in date.split(".")]
        return (y - 2000) * 12 * 28 + (m * 28) + d
    
    today = to_day(today)
    # print(today)
    
    # terms
    terms_dict = {i.split()[0] : int(i.split()[1]) * 28 for i in terms}
    # terms_dict = {}
    # for i in terms:
    #     key, value = i.split()
    #     terms_dict[key] = int(value)
    # print(terms_dict)

    for i, v in enumerate(privacies):
        join_date, type = v.split()
        end_day = to_day(join_date) + terms_dict[type]
        # print(today, end_day)
        if today >= end_day:
            answer.append(i+1)
        
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
#[1, 3]