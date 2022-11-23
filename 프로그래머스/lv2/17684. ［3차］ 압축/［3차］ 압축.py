def solution(msg):
    plus_idx = ['']
    result = []
    w = msg[0]
    for i in range(1, len(msg)):
        # print(w, msg[i])
        if w + msg[i] in plus_idx[1:]:
            w += msg[i]
        else:
            if len(w) == 1:
                result.append(ord(w) - ord('A') + 1)
            else:
                result.append(plus_idx.index(w) + 26)
            plus_idx.append(w + msg[i])
            w = msg[i]
            
    if len(w) == 1:
        result.append(ord(w) - ord('A') + 1)
    else:
        result.append(plus_idx.index(w) + 26)
    return result