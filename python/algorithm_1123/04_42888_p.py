def solution(record):
    answer = []
    user_info = {}
    for i in record:
        command, uid, *_ = i.split()
        if command == 'Enter':
            nickname = i.split()[2]
            user_info[uid] = nickname
        elif command == 'Leave':
            pass
        elif command == 'Change':
            nickname = i.split()[2]
            user_info[uid] = nickname


    for i in record:
        command, uid, *_ = i.split()
        if command == "Enter":
            answer.append(user_info[uid] + "님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(user_info[uid] + "님이 나갔습니다.")

        # if len(temp) == 3:
        #     user_nick = temp[2]
        #     record_dict[user_id] = {'nickname' : user_nick}
        # record_dict[user_id]['status'] = status
        # print(record_dict)
        # if status == 'Enter':
        #     str = f'{record_dict[user_id]['nickname']}이 들어오셨습니다.'
        # elif status == 'Leave':
        #     str = f'{record_dict[user_id]['nickname']}이 나가셨습니다.'
        # print(str)
        # answer.append(str)
    # print(user_info)
    return answer

record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"]
print(solution(record)) 