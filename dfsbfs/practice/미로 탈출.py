# # N X M 미로에서 (1,1) -> (N,M)로 괴물을 피해 탈출하기, 괴물은 0, 없으면 1
# # 한칸 이동할 때 마다 1씩 증가할 때, 최소한의 step을 구해라 (BFS)
#
# # 내 풀이
# from collections import deque
#
# # 세로(n), 가로(m) 개수 입력받기
# n, m = map(int, input().split())
#
# # n개의 줄로 미로정보 입력받기
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
#
# # 방문처리 정보
# visited = [[False] * m for _ in range(n)]
#
# # 상하좌우 이동
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# # bfs 정의
# def bfs(x, y):
#     # 미로정보 : 괴물(0), 빈곳(1)
#     # 시작지점 넣어주기 (x, y) 형태로 들어감
#     q = deque([(x, y)])
#     # 시작지점 방문처리
#     visited[x][y] = True
#     # 큐가 빌때까지
#     while q:
#         x, y = q.popleft()
#         # 상하좌우로 이동해보자
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 범위를 벗어나거나 방문했는지 검사 + 괴물이 아닌지
#             if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0 or visited[nx][ny]:
#                 continue
#             # 그게 아니라면 방문처리 하고 이전값에 +1로 저장하기
#             visited[nx][ny] = True
#             q.append((nx, ny))
#             graph[nx][ny] = graph[x][y] + 1
#
# # 시작지점은 (0.0)으로 상하좌우 이동해보기
# bfs(0, 0)
#
# # 마지막 지점 출력
# print(graph[n - 1][m - 1])

# 해설지 풀이
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
print(graph)
