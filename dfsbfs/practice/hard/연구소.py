# 연구소에 바이러스가 퍼지는 데, 벽이 있으면 그 이상 넘어가지 못한다.
# 임의의 벽 3개를 세웠을 때, 안전영역(바이러스가 퍼지지 않은 공간)의 최대값을 구하라

from itertools import combinations
import copy

# 세로크기(n), 가로크기(m) 입력받기
n, m = map(int, input().split())

# 연구소 정보 입력받기 : 0은 빈 칸, 1은 벽, 2는 바이러스
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 빈칸인 부분의 정보를 저장해놓고 컴비네이션으로 3개씩 경우의 수 구하기
empty_space_info = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_space_info.append((i, j))

wall_info = list(combinations(empty_space_info, 3))

# 맵 정보가 주어졌을 때, 안전영역 구하는 함수(재귀함수)
def dfs(temp_graph, x, y):
    global n, m
    # 범위를 벗어나거나 빈 칸이 아니라면 함수 종료
    if x < 0 or x >= n or y < 0 or y >= m or temp_graph[x][y] != 0:
        return
    # 해당 위치가 빈칸일 때만 바이러스 퍼뜨리고 재귀돌리기
    # 바이러스로 변경하고, 상하좌우로 이동해보기
    temp_graph[x][y] = 2
    dfs(temp_graph, x - 1, y)
    dfs(temp_graph, x + 1, y)
    dfs(temp_graph, x, y - 1)
    dfs(temp_graph, x, y + 1)

# 안전영역 구하는 함수
def get_safe_area(d):
    cnt = 0
    for x in range(len(d)):
        for y in range(len(d[x])):
            if d[x][y] == 0:
                cnt += 1
    return cnt

# 임의의 벽정보 돌면서 3개씩 세워보고 안전영역 구해보기
answer = -1
for temp_wall in wall_info:
    temp_graph = copy.deepcopy(graph)
    # 벽 세울 정보 돌면서 해당 위치에 벽세우기
    for tw in temp_wall:
        x, y = tw
        temp_graph[x][y] = 1
    # 전체 맵을 돌아보자
    # visited = [[False] * (m + 1) for _ in range(n + 1)]
    for x in range(n):
        for y in range(m):
            # 만약 바이러스라면 상하좌우로 퍼뜨려보자
            if temp_graph[x][y] == 2:
                dfs(temp_graph, x - 1, y)
                dfs(temp_graph, x + 1, y)
                dfs(temp_graph, x, y - 1)
                dfs(temp_graph, x, y + 1)
    result = get_safe_area(temp_graph)
    answer = max(answer, result)

print(answer)
