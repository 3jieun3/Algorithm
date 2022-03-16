def sizeRank(n, array):
    arr = array
    # 키, 몸무게 둘다 큰 사람의 수 + 1
    for i in range(n):
        rank = 0
        for j in range(n):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: 
                rank += 1
        arr[i].append(rank+1)
    return arr

n = int(input())
people = []

for i in range(n):
    people.append(list(map(int, input().split())))

people = sizeRank(n, people)
for j in range(n):
    print(people[j][2], end = ' ')