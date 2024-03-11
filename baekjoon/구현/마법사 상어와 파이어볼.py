# 마법사 상어가 파이어볼을 이동하고, 남아있는 파이어볼의 질량의 합 구하기

# 격자 크기 N, 파이어볼의 개수 M, 이동 갯수 K 입력
n, m, k = map(int, input().split())
# N X N 그래프 생성 (각 위치는 []을 가지고 있는다..?)
graph = [[] for _ in range(n * n)]
# M개의 파이어볼 정보 입력
fireballs = []
for _ in range(m):
    # (r, c) 위치에 질량(m), 속력(s), 방향(d)를 가지고 있는다.
    r, c, m, s, d = map(int, input().split())
    graph[(r - 1) * n + (c - 1)].append((m, s, d))

# 격자 크기와 현재 위치 (x,y), 각각 이동해야 하는 값 주어졌을 때, 위치 구해주기 (순환처리)
def get_pos(x, y, dx, dy):
    global n
    # 2. 구한 값만큼 이동해보기
    nx = x + dx
    ny = y + dy
    # 3. 범위가 벗어나는 경우를 check해주기
    # 3-1. 음수인 경우, n 더해주기
    if nx < 0:
        nx += n
    # 3-2. n을 이상인 경우 경우, n을 빼주기
    elif nx >= n:
        nx -= n

    # 3-1. 음수인 경우, n 더해주기
    if ny < 0:
        ny += n
    # 3-2. n을 이상인 경우 경우, n을 빼주기
    elif ny >= n:
        ny -= n
    # 이동한 위치 리턴하기
    return (nx, ny)

# 12시방향부터 시계방향으로 8가지 이동 방향 정의 (x, y)
steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# k번 반복 수행 내용
for t in range(k):
    # 1. 각각 이동시키기 임시공간을 만들고 해당 위치에 이동시키기
    temp_graph = [[] for _ in range(n * n)]
    for x in range(n):
        for y in range(n):
            # 여러개의 파이어볼이 들어있을 수 있는 배열 접근
            for data in graph[x * n + y]:
                m, s, d = data
                # 속력(s)만큼 d방향으로 이동시키기
                dx = steps[d][0] * (s % n)
                dy = steps[d][1] * (s % n)
                # 범위를 벗어나면, 격자를 나간 파이어볼로 순환시켜주기
                nx, ny = get_pos(x, y, dx, dy)
                temp_graph[nx * n + ny].append((m, s, d))

    # 2. 이동이 끝났다면, 각 위치에 두개 이상의 파이어볼을 합치고 4개로 다시 분리하는 작업 수행
    for x in range(n):
        for y in range(n):
            # 해당 위치에 2개 이상의 파이어볼이 존재한다면, 합치기 -> 4개로 분리하는 작업 수행
            if len(temp_graph[x * n + y]) >= 2:
                # 질량, 속력, 방향의 합 구해보기
                m_sum = 0
                s_sum = 0
                d_sum = 0
                is_odd = True
                is_even = True
                for m, s, d in temp_graph[x * n + y]:
                    m_sum += m
                    s_sum += s
                    # 짝수라면, 홀수는 False
                    if d % 2 == 0:
                        is_odd = False
                    # 홀수라면, 짝수는 False
                    else:
                        is_even = False
                # 4개의 파이어볼로 나누었을 때 값 구해보기
                m_avg = m_sum // 5
                # 질량이 0이라면 소멸
                if m_avg == 0:
                    temp_graph[x * n + y] = []
                    continue
                s_avg = s_sum // len(temp_graph[x * n + y])
                d_arr = []
                # 모든 방향이 짝수이거나, 홀수라면
                if is_odd or is_even:
                    d_arr = [0, 2, 4, 6]
                else:
                    d_arr = [1, 3, 5, 7]
                # 4개의 파이어볼 결과 생성하여 넣어주기
                result = []
                for i in range(4):
                    result.append((m_avg, s_avg, d_arr[i]))
                temp_graph[x * n + y] = result
    # graph 갱신해주기
    graph = temp_graph

# 남아있는 질량의 합 구해보기
answer = 0
for x in range(n):
    for y in range(n):
        if len(graph[x * n + y]) > 0:
            for data in graph[x * n + y]:
                m, s, d = data
                answer += m

# 정답 출력
print(answer)
