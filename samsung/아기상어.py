from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 현재 위치 알아 내기
cur_pos = (0, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            cur_pos = (i, j)
            graph[i][j] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cur_size = 2
fee_cnt = 0
eat_cnt = 0
sec = 0

while True:
    fee_cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] < cur_size:
                fee_cnt += 1
    if fee_cnt == 0:
        break
    else:
        d = [[-1] * n for _ in range(n)]
        q = deque()
        y, x = cur_pos
        d[y][x] = 0
        q.append((y, x))
        poss_fee = []
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n or d[ny][nx] != -1 or graph[ny][nx] > cur_size:
                    continue
                elif 0 < graph[ny][nx] < cur_size:
                    poss_fee.append((d[y][x] + 1, ny, nx))
                d[ny][nx] = d[y][x] + 1
                q.append((ny, nx))
        if len(poss_fee) == 0:
            break
        else:
            poss_fee.sort()
            distance, y, x = poss_fee[0]
            graph[cur_pos[0]][cur_pos[1]] = 0
            cur_pos = (y, x)
            eat_cnt += 1
            sec += distance
            if cur_size <= eat_cnt:
                cur_size += 1
                eat_cnt = 0

print(sec)
