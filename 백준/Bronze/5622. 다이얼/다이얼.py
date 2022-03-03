s = list(input())
# 문자에 해당하는 숫자는 각 인덱스 +2
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = len(s)

# 다이얼 돌리는 시간 = 각 숫자 +1 초
# 알파벳에 해당하는 숫자 찾기 -> 총합+입력문자갯수
for x in s:
    for y in dial:
        if x in y:  # if '지정문자열' in '문자열'
            sec += dial.index(y)+2

print(sec)