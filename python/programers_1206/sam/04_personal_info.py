def solution(today, terms, privacies):
    def calc_days(date):
        y, m, d = [int(i) for i in date.split(".")]
        return (y - 2000) * 28 * 12 + m * 28 + d

    answer = []
    today = calc_days(today)
    
    term_dict = {i.split()[0]: int(i.split()[1]) * 28 for i in terms}
    # term_dict = {}
    # for i in terms:
    #     type, period = i.split()
    #     term_dict[type] = int(period * 28)
    
    for i, v in enumerate(privacies):
        collected_date, type = v.split()
        collected_date = calc_days(collected_date)
        period = term_dict[type]
        if today - period >= collected_date:
            answer.append(i+1)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))