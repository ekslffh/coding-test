# 어른 상어
import copy

# 격자 크기 N, 상어 개수 M, 냄새 유지 시간 K 입력
n, m, k = map(int, input().split())

# 격자 정보 입력
graph = [[[0, 0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] > 0:
            graph[i][j] = [data[j], k]

# 상어별 현재 방향 입력
sharks = list(map(int, input().split()))

# 상어별 방향별 우선순위 입력 1(위), 2(아래), 3(왼), 4(오)
priorities = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priorities[i].append(list(map(int, input().split())))

# 위, 아래, 왼, 오 순으로 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 상어의 이동방향 나타내기
def move_shark(num, x, y, prev_map):
    # 상어의 현재 방향 찾기
    cur_d = sharks[num - 1]
    prev = []
    result = []
    # 상어의 방향별 우선순위를 토대로 다음 방향 찾기
    for dn in priorities[num - 1][cur_d - 1]:
        # 이동할 방향 잡기
        nx = x + dx[dn - 1]
        ny = y + dy[dn - 1]
        # 범위 검사
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 다른 상어의 냄새가 존재하는지 검사
        elif prev_map[nx][ny][1] > 0:
            # 자신의 냄새면 우선 prev에 저장하기
            if prev_map[nx][ny][0] == num:
                prev.append((nx, ny, dn))
            continue
        # 여기까지 왔으면 해당 칸은 빈칸이므로 이동 가능
        # 방향을 그대로 설정해주고 리턴하기
        sharks[num - 1] = dn
        return (nx, ny)
    # 여기라면 가능한 빈칸이 없었기 때문에 이전의 이동했던 곳으로 다시 가기
    sx, sy, sd = prev[0]
    sharks[num - 1] = sd
    return (sx, sy)

# 상어가 1마리, 즉 1번 상어만 남을 때까지 반복해보기
cnt = m
second = 0
while cnt > 1:
    prev_map = copy.deepcopy(graph)
    second += 1
    if second > 1000:
        break
    # 다음 상어 위치 정보
    next_sharks = []
    # 그래프 돌면서 상어 이동 정보 저장
    for x in range(n):
        for y in range(n):
            if graph[x][y][0] > 0:
                # 현재 상어가 존재한다면, 1번 인덱스가 k일 것이다.
                if graph[x][y][1] == k:
                    # 상하좌우 이동 수행
                    sx, sy = move_shark(graph[x][y][0], x, y, prev_map)
                    # (상어번호, x좌표, y좌표)
                    next_sharks.append((graph[x][y][0], sx, sy))
                # 냄새 유지 기간 줄이기
                graph[x][y][1] -= 1
    # 상어 이동 정보에 따른 이동하기
    for num, x, y in next_sharks:
        # 해당 위치에 다른 상어가 존재한다면 : 1번 인덱스가 k일 것이다.
        # 이러한 경우, 번호가 낮은 친구가 살아남는다.
        if graph[x][y][1] == k:
            # 번호가 더 작은 상어가 살아남는다.
            graph[x][y][0] = min(graph[x][y][0], num)
            # 싸울 때마다 한마리씩 쫓겨나는 구조
            cnt -= 1
        # 빈칸잉거나, 자신의 냄새가 존재하는 경우, 그대로 덮어쓰기
        else:
            graph[x][y] = [num, k]

if second > 1000:
    print(-1)
else:
    print(second)
