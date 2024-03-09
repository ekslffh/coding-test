# 전형적인, 시뮬레이션 문제이다.
# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수 구하기.

# 세로 길이 N, 가로 길이 M 입력 받기
n, m = map(int, input().split())
# 로봇 청소기 위치 (r, c)와 방향 (0,0 부터 시작), d 입력 받기 (0:북, 1:동, 2:남, 3:서)
r, c, d = map(int, input().split())
# N개의 줄에 방의 상태 입력 받기 (0:빈칸, 1:벽)
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 필요 데이터 방향 설정 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계 방향으로 90도 회전하면 북 -> 서 -> 남 -> 동
def rotation():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

# 시뮬레이션 돌리기
x, y = r, c
nx, ny = x, y
# 청소구역 세기
answer = 0
# 회전 횟수 구하기
cnt = 0
while True:
    # 현재 칸이 청소되어 있지 않으면 청소하기
    if graph[nx][ny] == 0:
        # 청소한 곳은 2로 변경
        graph[nx][ny] = 2
        # 현재 위치 전진한 위치로 변경
        x, y = nx, ny
        # 회전 횟수 초기화
        cnt = 0
        # 청소개수 올려주기
        answer += 1
    # 그게 아닐 때, 회전 검사해보기
    else:
        # 4칸 중 갈곳이 없다면 후진하기
        if cnt >= 4:
            # 후진 시 뒤에 벽이라면 시뮬종료
            nx = x - dx[d]
            ny = y - dy[d]
            # 벽이라면 게임 종료
            if graph[nx][ny] == 1:
                break
            # 그게 아니라면 후진하고 카운트 초기화
            else:
                x, y = nx, ny
                cnt = 0
    # 두가지 모두, 회전은 감행해야 한다.
    rotation()
    # 방향에 맞게 nx, ny 지정해보기
    nx = x + dx[d]
    ny = y + dy[d]
    # 회전 횟수 올려주기
    cnt += 1

# 정답 출력
print(answer)
