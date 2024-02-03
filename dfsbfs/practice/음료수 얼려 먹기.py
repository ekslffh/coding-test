# # N X M 크기의 얼음틀에 뚫려있는 부분(0)과 칸막이가 있는 부분(1)이 존재할 때 생성되는 아이스크림의 개수 출력하기
# # 한 곳을 기점으로 뚫려 있는 부분 전체 탐색하여서 방문처리 하기
#
# # 세로길이(N), 가로길이(M) 입력받기
# n, m = map(int, input().split())
# # N개의 줄에서 얼음 틀의 정보 입력받기
# graph = []
# for _ in range(n):
#     data = list(map(int, input()))
#     graph.append(data)
# # 방문처리 할 변수 선언
# visited = [[False] * m for _ in range(n)]
#
# # 깊이 우선 탐색
# def dfs(graph, x, y, visited):
#     # 종료조건 명시
#     # 1. 범위를 벗어난 경우
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return
#     # 2. 칸막이가 존재하는 경우
#     elif graph[x][y] == 1:
#         return
#     # 3. 이미 방문한 경
#     elif visited[x][y]:
#         return
#     # 현재 들어온 녀석 방문처리
#     visited[x][y] = True
#     # 상하좌우로 이동해서 재귀함수 돌리기
#     dfs(graph, x - 1, y, visited)
#     dfs(graph, x + 1, y, visited)
#     dfs(graph, x, y - 1, visited)
#     dfs(graph, x, y + 1, visited)
#
# # 처음부터 끝까지 반복하면서 방문처리가 안되어있으면 카운팅하고 연결되어 있는 부분 전부 처리하기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 빈곳 중 방문하지 않은 곳이 있다면 카운팅하고 연결된 부분 재귀돌리기
#         if graph[i][j] == 0 and not visited[i][j]:
#             result += 1
#             dfs(graph, i, j, visited)
#
# print(result)

# N, M을 공백으로 구분하여 입력하기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
