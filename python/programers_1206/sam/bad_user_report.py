from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = defaultdict(list)
    bad_users_dict = defaultdict(int)
    report = set(report)
    stop_users = []
    for i in report:
        report_user, bad_user = i.split()
        report_dict[bad_user].append(report_user)
        bad_users_dict[bad_user] += 1
        if bad_users_dict[bad_user] == k:
            stop_users.append(bad_user)
    for i in stop_users:
        for j in range(len(id_list)):
            if id_list[j] in report_dict[i]: 
                answer[j] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)