# # 시뮬레이션 게임
#
# # 세로크기 N과 가로크기 M 입력받기
# n, m = map(int, input().split())
# # 게임좌표와 방향 입력받기 (시작은 항상 육지이다)
# x, y, d = map(int, input().split())
# # 맵 정보 입력받기 (육지는 0, 바다는 1)
# graph = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)
#
# # 방향에 따른 이동값 정의하기 0: 북, 1: 동, 2: 남, 3: 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 반복해서 처리하는데 먼저 반시계로 왼쪽방향부터 갈 수 있는지 확인하면서 가보고 4방향 다 가봤으면 뒤로 이동해보는데 뒤가 바다이면 반복 종료
#
# # 반시계로 회전하는 함수
# def rotation(direction):
#     # 북 -> 서 -> 남 -> 동 : 즉 -1씩
#     if direction == 0:
#         return 3
#     else:
#         return direction - 1
#
#
# result = 1
# # 회전 횟수 세는 변수
# r_cnt = 0
#
# # 시작지점 미리 방문처리
# graph[x][y] = 2
#
# while True:
#     # 4방향 모두 돌았다면 뒤로 이동해보기
#     if r_cnt >= 4:
#         nx = x - dx[d]
#         ny = y - dy[d]
#         # # 범위를 벗어나는지 검사 (외곽이 항상 바다이기 때문에 범위검사 필요없음)
#         # if nx < 0 or nx >= n or ny < 0 or ny >= m:
#         #     break
#         # 뒤에가 바다라면 나가기
#         if graph[nx][ny] == 1:
#             break
#         # 둘다 아니라면, 이동하고 회전횟수 0, 방문처리는 필요없음(어차피 무조건 방문했던 데라 여기로 온거니껜)
#         else:
#             x, y = nx, ny
#             r_cnt = 0
#
#     # 반시계 회전하고 회전횟수 증가시키기
#     d = rotation(d)
#     r_cnt += 1
#     nx = x + dx[d]
#     ny = y + dy[d]
#     # # 범위를 벗어나는지 검사하기
#     # if nx < 0 or nx >= n or ny < 0 or ny >= m:
#     #     continue
#     # 안가본 곳이라면 이동하고 방문처리(2) 회전횟수 0으로 초기화, 가본곳으로 카운팅
#     if graph[nx][ny] == 0:
#         result += 1
#         x, y = nx, ny
#         graph[x][y] = 2
#         r_cnt = 0
#
# print(result)

# 해설 풀이
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
