import math

def solution(n, stations, w):
    # 기지국 설치해보기
    def build_station(x, v):
        v[x] = True
        for i in range(1, w + 1):
            l = x - i
            r = x + i
            if l >= 1 and not v[l]:
                v[l] = True
            if r <= n and not v[r]:
                v[r] = True

    # 추후에 기지국 개수 더해주기
    answer = 0

    result = []
    # 기지국 정보 돌면서 전파 전달 검사
    start = 1
    for s in stations:
        # s에 설치했을 때, 커버 범위 구해보기
        cs, ce = max(s - w, 1), min(s + w, n)
        if start < cs:
            result.append(cs - start)
        # 커버 못한 ce부터 시작점 잡기
        start = ce + 1
    if start <= n:
        result.append(n - start + 1)

    # 현재 기지국 설치 이후의 도달안된 범위들 배열
    for cnt in result:
        # w에 따른 커버가능 시작 개수 찾기
        t = w * 2 + 1
        # (필요한 기지국 개수는 범위 / t)의 올림결과
        req_station_cnt = math.ceil(cnt / t)
        answer += req_station_cnt

    return answer

print(solution(11, [4, 11], 1))
