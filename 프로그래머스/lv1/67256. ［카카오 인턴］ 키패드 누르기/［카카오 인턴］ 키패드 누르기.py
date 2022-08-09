keys = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

def solution(numbers, hand):
    l_pos, r_pos = [0, 3], [2, 3]
    result = ""
    
    for i in range(len(numbers)):
        num = numbers[i]
        if num == 0:
            num = 11
        # 왼쪽
        if (num % 3) == 1:
            result += "L"
            l_pos = [0, keys[0].index(num)]
        # 오른쪽
        elif (num % 3) == 0:
            result += "R"
            r_pos = [2, keys[2].index(num)]
        # 중간
        else:
            idx = keys[1].index(num)
            l_diff = abs(l_pos[0] - 1) + abs(l_pos[1] - idx)
            r_diff = abs(r_pos[0] - 1) + abs(r_pos[1] - idx)
            # 왼손
            if l_diff < r_diff or (l_diff == r_diff and hand == "left"):
                result += "L"
                l_pos = [1, idx]
            # 오른손
            elif l_diff > r_diff or (l_diff == r_diff and hand == "right"):
                result += "R"
                r_pos = [1, idx]
        
    return result