n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

horses = []
horses_map = [[[] for _ in range(n)]for _ in range(n)]
# 어떤 위치에 : 몇번 말이 들어있음
for i in range(1, k + 1):
    x, y, d = list(map(int, input().split()))
    horses.append([x - 1, y - 1, d])
    horses_map[x - 1][y - 1].append(i)

# (x, y)
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 게임 시작
turn = 1
while True:
    is_over = False
    for i in range(len(horses)):
        x, y, d = horses[i]
        nx = x + direction[d - 1][0]
        ny = y + direction[d - 1][1]
        # 범위를 벗어나거나, 해당 칸이 파란색이라면 반대 방향으로 바꾸기
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            else:
                d = 3
            # 다시 위치를 잡아주기
            nx = x + direction[d - 1][0]
            ny = y + direction[d - 1][1]
            # 방향 바꿔주기
            horses[i][2] = d
            # 반대 방향도 갈 수 없다면, 그대로 멈추기 (더이상 움직일 수 없는 말이다)
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
                continue
        # 여기서 내 위에 쌓인 데이터만 같이 간다.
        find_idx = 0
        for idx in range(len(horses_map[x][y])):
            if horses_map[x][y][idx] == i + 1:
                find_idx = idx
        # find_idx를 기준으로 나누기
        right = horses_map[x][y][find_idx:]
        horses_map[x][y] = horses_map[x][y][:find_idx]
        # 빨간색 칸이라면 거꾸로 만들어주기
        if graph[nx][ny] == 1:
            right.reverse()
        # 그대로 이동해보는데, 해당 자리에 이미 말들이 있다면 그 위로 쌓기
        horses_map[nx][ny].extend(right)
        # 말 위치, 방향 갱신 (방향만 그대로)
        for number in right:
            horses[number - 1][0], horses[number - 1][1] = nx, ny
        # 기존 값 지우기
        if len(horses_map[nx][ny]) >= 4:
            is_over = True
            break
    # 종료조건 (말이 4개이상 쌓이거나, 1000번 넘었거나, 움직일 수 있는 말이 없을 때)
    if is_over or turn >= 1000:
        break
    turn += 1

if turn >= 1000:
    print(-1)
else:
    print(turn)
