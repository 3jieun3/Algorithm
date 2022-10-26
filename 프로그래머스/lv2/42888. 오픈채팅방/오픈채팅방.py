def solution(record):
    
    answer = []
    history = []
    nicknames = {}
    
    for i in range(len(record)):
        if record[i].startswith('Enter'):
            act, uid, nickname = record[i].split()
            history.append([uid, "님이 들어왔습니다."])
            nicknames[uid] = nickname
            
        elif record[i].startswith('Leave'):
            act, uid = record[i].split()
            history.append([uid, "님이 나갔습니다."])
        else:
            act, uid, nickname = record[i].split()
            nicknames[uid] = nickname
    
    for uid, act in history:
        answer.append(nicknames[uid] + act)
                
    return answer