# LRU : 가장 오랫동안 사용하지 않는 캐시를 삭제하는 캐시 교체 알고리즘
def solution(cacheSize, cities):
    tot_time = 0
    cache = []
    cnt = 0
    for city in cities:
        # 대소문자 구분 없앰
        city = city.upper()
        
        # 캐시 사이즈 0인 경우
        if cacheSize == 0:
            tot_time += 5
            continue
            
        # cache hit
        if city in cache:
            tot_time += 1
            idx = cache.index(city)
            cache.pop(idx)
            cache.append(city)
            
        # cache miss
        else:
            tot_time += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        
        # print(city, cache, tot_time)
    return tot_time