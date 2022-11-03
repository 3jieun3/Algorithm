# 누적 주차 시간 계산
def calcul_mins(h1, m1, h2, m2):
    if m1 <= m2:
        return (h2 - h1) * 60 + (m2 - m1)
    return (h2 - 1 - h1) * 60 + (m2 + 60 - m1)

# 주차 요금 계산
def calcul_fee(mins, fees):
    tot = fees[1]
    if mins > fees[0]:
        mins -= fees[0]
        if mins % fees[2]:
            tot += (mins // fees[2] + 1) * fees[3]
        else:
            tot += (mins // fees[2]) * fees[3]
    return tot

def solution(fees, records):
    # 차 번호 오름차순 저장
    cars = []
    for record in records:
        cars.append(record.split()[1])
    cars = sorted(list(set(cars)))
    cnt = len(cars)
    print(cars)
    time_records = [[''] * 24 for _ in range(cnt)]  # [i][j] = i번 자동차가 j시에 입차한 분 정보
    status = [-1] * cnt    # [i] = i번 차가 들어왔던 시간
    answer = [0] * cnt
    
    for record in records:
        time, num, stat = record.split()
        hour, mins = map(int, time.split(':'))
        idx = cars.index(num)
        # 출차
        if stat == 'OUT':
            h = status[idx]
            answer[idx] += calcul_mins(h, time_records[idx][h], hour, mins)
            status[idx] = -1
            time_records[idx][h] = ''
        # 입차
        else:
            status[idx] = hour
            time_records[idx][hour] = mins
    
    # 남아있는 차 확인
    for idx in range(cnt):
        if status[idx] != -1:
            h = status[idx]
            answer[idx] += calcul_mins(h, time_records[idx][h], 23, 59)
    
    
    # 주차 요금 계산
    for idx in range(cnt):
        answer[idx] = calcul_fee(answer[idx], fees)
        
    return answer