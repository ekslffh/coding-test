# 출발지점에서 목표지점까지의 최적의 경로를 찾기
# 상하좌우로 움직이면서 현재 값을 갱신해주는 형태로 구현해보기
from collections import deque

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

t = int(input())

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # 각 위치별 최단 거리 구해보기
    # 시작점인 0,0은 해당 거리로 초기화
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    q = deque([(0, 0)])
    while q: # 큐가 빌 때까지
        x, y = q.popleft()
        # 상하좌우 이동해보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는지 검사
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 범위를 벗어나지 않는다면 발생 비용 구해보기
            # 현재 x, y를 기준으로 nx, ny로 이동하는 것
            cost = distance[x][y] + graph[nx][ny]
            # 만약 발생비용이 기존의 distance보다 작다면 갱신해주고 큐에 넣어주기
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                q.append((nx, ny))
    # 목표지점 위치 찍어주기
    for i in range(n):
        for j in range(n):
            print(distance[i][j], end=' ')
        print()
    print(distance[n - 1][n - 1])
