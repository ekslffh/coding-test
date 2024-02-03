# 1 ~ K 종류의 바이러스 존재할 때, 작은 번호의 바이러스부터 상하좌우로 증식해 나간다.
# 다른 바이러스가 없는 0인 공간에만 증식이 가능할 때, S초가 지난 후에 (X, Y)의 바이러스 종류는?

# 시험관 크기(N), 바이러스 종류(K) 입력받기
n, k = map(int, input().split())
# 시험관 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 바이러스 정보 저장해놓기 (종류, x좌표, y좌표)
virus_info = []
for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            virus_info.append((graph[x][y], x, y))
# 초(S), X, Y 입력받기
s, x, y = map(int, input().split())
# 증식해보자
arr = sorted(virus_info)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상하좌우 증식해보기
def infection(k, x, y, v_info):
    global n
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나거나, 빈곳이 아니라면 continue
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
            continue
        # 그게 아니라면 해당 위치에 k-virus 증식
        graph[nx][ny] = k
        v_info.append((k, nx, ny))

for i in range(s):
    virus_info.sort()
    v_info = []
    for virus in virus_info:
        vk, vx, vy = virus
        infection(vk, vx, vy, v_info)
    virus_info = v_info

print(graph[x - 1][y - 1])
