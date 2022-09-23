def calcul_time(h1, m1, h2, m2):
    if m1 <= m2:
        return (h2 - h1) * 60 + (m2 - m1)
    else:
        return (h2 - 1 - h1) * 60 + (m2 + 60 - m1)

def calcul_fee(tot, fees):
    # fees : 기본분, 기본원, 단위분, 단위원
    fee = fees[1]
    if tot <= fees[0]:
        return fee
    else:
        tot -= fees[0]
        if tot % fees[2]:
            fee += (tot // fees[2] + 1) * fees[3]
        else:
            fee += (tot // fees[2]) * fees[3]
        return fee
    
def solution(fees, records):
    cars = []
    for i in range(len(records)):
        time, car, stat = records[i].split()
        cars.append(car)
        
    cars = list(set(cars))
    cars.sort()
    cnt = len(cars)
    
    times = [[''] * 24 for _ in range(cnt)]
    status = [-1] * cnt
    total_mins = [0] * cnt
    
    for i in range(len(records)):
        time, car, stat = records[i].split()
        h, m = time.split(':')
        idx = cars.index(car)
        
        if stat == "OUT":       # 출차
            for j in range(int(h) + 1):
                if times[idx][j]:
                    total_mins[idx] += calcul_time(j, int(times[idx][j]), int(h), int(m))
                    times[idx][j] = ''
                    status[idx] = -1
        else:                   # 입차
            times[idx][int(h)] += m
            status[idx] = int(h)
            
    # 23:59 출차 간주
    for i in range(cnt):
        if status[i] != -1:
            h = status[i]
            total_mins[i] += calcul_time(h, int(times[i][h]), 23, 59)
            times[i][h] = ''
            status[i] = -1
    
    # 요금 계산
    
    fee_arr = [0] * cnt
    for i in range(cnt):
        fee_arr[i] = calcul_fee(total_mins[i], fees)
    
    return fee_arr