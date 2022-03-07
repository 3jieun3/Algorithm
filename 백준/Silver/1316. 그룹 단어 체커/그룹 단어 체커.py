# 다른방법 #
n = int(input())
group = 0
for _ in range(n):
    word = input()  # abbcccab
    error = 0
    # word에서 연속한 중복 이외에 따로 떨어진 중복 횟수 카운트
    for i in range(len(word)-1):
        if word[i] != word[i+1]: # 연달아 두 문자가 다를 경우 ex) ab...
            new = word[i+1:] # 현재 위치 이후의 문자열을 새로운 단어 new 로 생성
            if new.count(word[i])>0: # new에서 현재 문자가 있다면
                error += 1
        else: continue  # 연달아 두 문자가 같은 경우 다음으로 ex) bb...
    
    # 한문자요소라도 따로 떨어진 중복 횟수가 존재한다면 그룹단어가 아님
    if error == 0: group += 1
    
print(group)