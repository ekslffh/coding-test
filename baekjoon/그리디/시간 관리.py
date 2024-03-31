# 아이디어 : 적어도 시작해야 하는 시간부터 -1하면서 최적의 시간 찾기

INF = int(1e9)

# 데이터 입력 t: 처리하는데 걸리는 시간, s: s시까지 끝내야 한다.
n = int(input())
data = []
# 적어도 시작해야 하는 시간 구하기
start_time = INF
for _ in range(n):
    t, s = map(int, input().split())
    start_time = min(start_time, s - t)
    data.append((t, s))

# 데이터 정렬, 1.s 기준 오름차순, t 기준 내림차순
data.sort(key=lambda x: (x[1], -x[0]))

while start_time >= 0:
    cur_time = start_time
    is_possible = True
    for t, s in data:
        cur_time += t
        if cur_time > s:
            is_possible = False
            break
    # 가능한 경우 나가고 start_time 출력해주기
    if is_possible:
        break
    # 1시 먼저 시작해보기
    start_time -= 1

# 정답 출력
if start_time < 0:
    print(-1)
else:
    print(start_time)
