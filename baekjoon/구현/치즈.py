# 모눈종이 위에 치즈가 있는데, 2번 이상이 공기와 접촉한다면 1시간 내로 녹아 없어질 때, 다 녹아지는 시간 구하기

from collections import deque

# 세로 길이 N, 가로길이 M 입력 받기
n, m = map(int, input().split())

# n개의 줄에 치즈 정보 입력 받기 (치즈 : 1, 아닌 부분은 0)
graph = []
# 치즈 개수 세보기
cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for x in graph[i]:
        if x == 1:
            cnt += 1

# 다 녹아 없어지는데 걸리는 시간 구해보기
answer = 0

# 상하좌우 방향
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

in_arr = [[True] * m for _ in range(n)] # 처음엔 True로 초기화하고 찾기

# bfs로 구현해보자
def find_insie(x, y):
    q = deque([(x, y)])
    # 큐가 빌 때까지 상하좌우로 이동해보기
    while q:
        cx, cy = q.popleft()
        for step in steps:
            nx = cx + step[0]
            ny = cy + step[1]
            # 범위 검사
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 해당 위치가 빈공간이면서, 방문하지 않았다면 큐에 넣어주기
            if graph[nx][ny] == 0 and in_arr[nx][ny]:
                q.append((nx, ny))
                # 방문처리도 해주기
                in_arr[nx][ny] = False

# 두변 이상이 외부 공기인 곳 찾아보기
def check_cheese(melt_arr):
    global n, m, cnt
    # 전체 맵을 돌면서 특정 치즈에 대하여 상하좌우 검사하기
    for x in range(1, n):
        for y in range(1, m):
            # 해당 위치가 치즈라면,
            if graph[x][y] == 1:
                empty_cnt = 0
                # 상하좌우 검사해보기
                for step in steps:
                    nx = x + step[0]
                    ny = y + step[1]
                    # 외부 공기 : 공백(0)이면서, 외부 공간일때!
                    if graph[nx][ny] == 0 and not in_arr[nx][ny]:
                        empty_cnt += 1
                # 공백이 2개 이상이라면, 치즈 녹아없어지고, 공백이 된다.
                if empty_cnt >= 2:
                    cnt -= 1
                    melt_arr.append((x, y))


# 치즈가 남아 있을 때까지 반복
while cnt > 0:
    # 내/외부 구분할 공간 배열 초기화 (처음엔 다 True로 내부로 지정)
    in_arr = [[True] * m for _ in range(n)]
    # 내/외부 공간 찾아보기 (0,0부터 찾기)
    find_insie(0, 0)
    # 시간 증가
    answer += 1
    # 녹아 없어질 치즈 넣어둘 배열
    melt_arr = []
    check_cheese(melt_arr)
    # 녹아 없어진 치즈 0으로 변경해주기 (검사가 다 끝난 이후에 변경해줘야 한다.)
    for x, y in melt_arr:
        graph[x][y] = 0

# 녹아 없어지는데, 걸린 시간 출력
print(answer)
