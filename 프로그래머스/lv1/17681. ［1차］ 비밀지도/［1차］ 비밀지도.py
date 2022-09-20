def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    for i in range(n):
        bin1 = list(map(int, bin(arr1[i]).lstrip('0b').zfill(n)))
        bin2 = list(map(int, bin(arr2[i]).lstrip('0b').zfill(n)))
        for j in range(n):
            if (bin1[j] | bin2[j]):
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer