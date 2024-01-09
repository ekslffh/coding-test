# 시뮬레이션 문제 : 캐릭터가 방문한 칸의 수를 출력하기

# 세로크기, 가로크기 입력받기
n, m = map(int, input().split())

# (a, b), 방향 d 입력받기
a, b, d = map(int, input().split())

# 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 북, 동, 남, 서 : -1씩 하면서 반시계로 돈다.
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change_direction(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

# y좌표 현재 위치 (0부터)
y = a
# x좌표 현재 위치 (0부터)
x = b
# 현재 시작위치 방문처리
graph[y][x] = 2
# 회전횟수 카운트
cnt = 0
# 시뮬레이션 대로 동작시키기
while True:
    # 4방향 모두 돌았으면 뒤로 가보기
    if cnt >= 4:
        by = y - dy[d]
        bx = x - dx[d]
        # 이동할 곳이 바다라면 게임 종료
        if graph[by][bx] == 1:
            break
        # 뒤로 이동하고 회전 카운트 초기화
        else:
            y, x = by, bx
            cnt = 0
    d = change_direction(d)
    cnt += 1
    ny = y + dy[d]
    nx = x + dx[d]
    # 범위를 벗어나면 continue
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
    # 방문하지 않았고 육지라면 이동하기
    if graph[ny][nx] == 0:
        # 방문한 곳으로 이동하고 2로 방문처리
        y, x = ny, nx
        graph[y][x] = 2
        # 이동했으면 회전카운트 0
        cnt = 0
    # 방문했거나 바다인 경우 다시 회전시켜야 함 : 그냥 반복 시키면 된다.

# 방문한 칸의 개수 세기 : 2인 녀석만 골라내면 됨
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            result += 1

# 정답출력
print(result)
print(graph)
