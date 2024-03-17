n, m, k = map(int, input().split())
graph = [[[0, 0] for _ in range(m)] for _ in range(m)]

cnt = 0
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] > 0:
            graph[i][j][0] = data[j]
            cnt += 1

shark = list(map(int, input().split()))

# 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽
shark_direction = [[] for _ in range(cnt)]
for i in range(cnt):
    for _ in range(4):
        shark_direction[i].append(list(map(int, input().split())))

d = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]

# 기존의 이미 들어와 있다면, 싸워서 번호가 낮은 친구가 이긴다.
def fight(x, y, num, t):
    # 누가 있는 경우, 번호를 기준으로 정하고 True 리턴
    if graph[x][y][1] == t:
        # num이 기존의 것보다 더 작으면 갱신
        if num < graph[x][y][0]:
            graph[x][y][0] = num
        # 아니면 그대로 유지
        return True
    # 아무도 없거나, 본인이라면 그냥 갱신하고 False 리턴
    else:
        graph[x][y] = [num, t]
        return False

t = 0
while cnt > 1:
    t += 1
    # 상어 이동
    for x in range(n):
        for y in range(m):
            if graph[x][y][0] > 0 and graph[x][y][1] == (t - 1):
                s_num = graph[x][y][0]
                s_cur_d = shark[s_num - 1]
                # 특정 상어의 특정 방향에 따른 방향 우선순위 돌면서
                ax, ay = -1, -1
                cur = []
                prev = []
                for direction in shark_direction[s_num - 1][s_cur_d - 1]:
                    dx, dy = d[direction]
                    nx = x + dx
                    ny = y + dy
                    # 범위 검사
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    # 해당 칸에 냄새가 남아 있으면 패스
                    if graph[nx][ny][0] != 0 and (t - graph[nx][ny][1]) < k:
                        # 혹시 돌아갈 것을 대비해 내 냄새 인지 체크하기
                        if graph[nx][ny][0] == s_num:
                            prev.append((nx, ny))
                        continue
                    cur.append((nx, ny))
                    break
                # 불가능 했다면, 이전에 있었던 공간으로 되돌아가기
                if len(cur) == 0:
                    ax, ay = prev[0]
                # 누군가 이미 글로 이동했으면 번호가 낮은 사람만 남음
                if fight(ax, ay, s_num, t):
                    cnt -= 1

print(t)
