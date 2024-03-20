# 마법사 상어와 파이어스톰
import copy
from collections import deque

# 격자 사이즈, 마법 횟수 입력
n, q = map(int, input().split())
# 2^n 사이즈의 그래프 정보 입력
graph = []
for _ in range(2 ** n):
    graph.append(list(map(int, input().split())))
# q개의 파이어스톰 정보 입력
fire_storms = list(map(int, input().split()))

# 상하좌우 방향
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 그래프를 2^l x 2^l 사이즈로 나누어서 시계방향 90도 회전
def rotate(l):
    global graph
    temp_graph = copy.deepcopy(graph)
    size = 2 ** l
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            # 몫과 나머지 저장
            mx, rx, my, ry = x // size, x % size, y // size, y % size
            # 나머지를 가지고 우선 회전 수행하고 몫만큼 다시 더해준다.
            nx = ry + (size * mx)
            ny = size - rx - 1 + (size * my)
            # 회전한 공간으로 값 갱신해주기
            temp_graph[nx][ny] = graph[x][y]
    # 그래프를 회전한 그래프로 갱신
    graph = temp_graph

# 연결되어 있는 얼음의 사이즈 구하기
def dfs(x, y, graph, visited, answer):
    answer.append(graph[x][y])
    visited[x][y] = True
    for dx, dy in steps:
        nx = x + dx
        ny = y + dy
        # 범위 검사
        if nx < 0 or nx >= 2 ** n or ny < 0 or ny >= 2 ** n:
            continue
        if graph[nx][ny] > 0 and not visited[nx][ny]:
            dfs(nx, ny, graph, visited, answer)

def bfs(x, y, graph, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    hap = 0
    while q:
        cx, cy = q.popleft()
        cnt += 1
        hap += graph[cx][cy]
        for dx, dy in steps:
            nx = cx + dx
            ny = cy + dy
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            if graph[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    # 얼음의 개수, 총합 리턴
    return (cnt, hap)

# 인접해 있는 칸의 3개 이상이 얼음이면 True 리턴
def check(x, y):
    global n, graph
    cnt = 0
    for dx, dy in steps:
        nx = x + dx
        ny = y + dy
        # 범위 검사
        if nx < 0 or nx >= 2 ** n or ny < 0 or ny >= 2 ** n:
            continue
        if graph[nx][ny] > 0:
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

# 파이어 스톰 수행
for l in fire_storms:
    # l기준 격자 나누어서, 회전 수행
    rotate(l)
    # 인접해 있는 칸 검사
    arr = []
    for x in range(2 ** n):
        for y in range(2 ** n):
            # 인접해 있는 얼음 칸이 3개 미만이라면, 얼음 녹이기
            if not check(x, y):
                arr.append((x, y))
    # 모든 검사가 수행된 이후에 얼음 녹이기
    for x, y in arr:
        graph[x][y] -= 1

visited = [[False] * (2 ** n) for _ in range(2 ** n)]

total = 0
result = 0
# 가장 큰 얼음의 사이즈 구해보기
for x in range(2 ** n):
    for y in range(2 ** n):
        if graph[x][y] > 0 and not visited[x][y]:
            cnt, hap = bfs(x, y, graph, visited)
            result = max(result, cnt)
            total += hap

print(total)
print(result)
