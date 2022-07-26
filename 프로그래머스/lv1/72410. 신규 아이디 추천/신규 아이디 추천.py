def solution(new_id):
    # 1
    tmp_id = new_id.lower()       
    # 2
    result_id = ''
    for tmp in tmp_id:
        if 'a' <= tmp <= 'z' or tmp.isdigit():
            result_id += tmp
        elif tmp in ['-', '_', '.']:
            # 3
            if tmp == '.':
                if result_id and result_id[-1] == '.':
                    continue
            result_id += tmp
    # 4
    result_id = result_id.strip('.')
    # 5
    if result_id == '':
        result_id += 'a'
    # 6
    result_id = result_id[:15].rstrip('.')
    # 7
    if result_id and len(result_id) <= 2:
        result_id += result_id[-1] * (3 - len(result_id))
    return result_id