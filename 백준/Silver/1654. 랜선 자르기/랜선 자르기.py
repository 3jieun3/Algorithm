#1  2  3  4 '5' 6 7 8 9  -> 1 + 2 + 3 + 4 = 10 < 14  | (1 5 9) -> (1 5 4)
#1 '2' 3  4              -> 4 + 5 + 9 + 10 = 28 > 14 | (1 2 4) -> (3 2 4)
#     '3' 4              -> 3 + 3 + 6 + 6 = 18 > 14  | (3 3 4) -> (4 3 4)
#        '4'             -> 2 + 2 + 4 + 5 = 13 < 14  | (4 4 4) -> (4 4 3)
k, n = map(int, input().split())
have = [int(input()) for _ in range(k)]
# maxlen <= min(have) 
startlen = 1
endlen = max(have)
while startlen <= endlen:
    cnt = 0
    mid = (startlen+endlen)//2
    for h in have:
        cnt += h//mid

    if cnt >= n: # == 더 크게 자르면 cnt 작아짐
        startlen = mid + 1
    else:
        endlen = mid - 1
print(endlen)