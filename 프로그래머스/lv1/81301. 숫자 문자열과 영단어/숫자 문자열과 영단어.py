arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = 0
    tmp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer = answer * 10 + int(s[i])
        else:
            tmp += s[i]
            if len(tmp) >= 3 and tmp in arr:
                answer = answer * 10 + arr.index(tmp)
                tmp = ''
                
    return answer