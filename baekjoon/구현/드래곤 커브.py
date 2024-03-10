# 드래곤 커브에 의해 만들어진 정사각형의 개수 구하기

# x,y의 최대크기인 100만큼의 그래프 배열 생성 하기
size = 100
graph = [[0] * (size + 1) for _ in range(size + 1)]

# 드래콘 커브의 개수 N 입력 받기
n = int(input())

# 드래곤 커브의 정보 입력받기
curves = []
for _ in range(n):
    # x, y를 시작점으로 하고 방향은 d인 g세대
    curves.append(list(map(int, input().split())))

# 특정 방향에 따른 다음 방향 구해주기
def get_next_direction(g):
    g += 1
    if g > 3:
        return 0
    else:
        return g

# 방향과 세대를 통해 이동 루트 구해주기
def find_route(direction, generation):
    # 0 세대는 시작점 하나만 가지고 있다.
    cur_g = [direction]
    # 세대만큼 반복하면서 경로 추가하기
    for _ in range(1, generation + 1):
        temp_g = []
        # 이전 세대의 경로를 거꾸로 하여서 다음 경로를 찾아주기
        for x in cur_g[::-1]:
            temp_g.append(get_next_direction(x))
        # 현재경로에 다음 경로 추가하면 다음 세대 경로가 된다.
        cur_g.extend(temp_g)
    return cur_g

# 경로에 따라 이동해보면서 graph 정보 갱신하기
def move_by_route(routes, x, y):
    # 시작점 방문 처리
    graph[x][y] = 1
    # 오른쪽 x축, 아래쪽 y축
    # 0 : right, 1 : up, 2 : left, 3 : down
    for route in routes:
        if route == 0:
            x += 1
        elif route == 1:
            y -= 1
        elif route == 2:
            x -= 1
        else: # route == 3
            y += 1
        # 이동한 곳 방문 처리
        graph[x][y] = 1

# 드래곤 커브 정보들 돌면서 수행
for curve in curves:
    # 시작점(x, y), 방향 d, 세대 g
    x, y, d, g = curve
    # 방향과 세대에 따른 이동경로 찾아보기
    routes = find_route(d, g)
    # 시작점부터 경로에 따라서 방문처리 하기
    move_by_route(routes, x, y)

# 현재 위치 기준으로, 1.오른쪽, 2. 아래쪽, 3. 우하 방향 찾아주기
steps = [(1, 0), (0, 1), (1, 1)]

# 0 ~ 100까지의 그래프 4꼭지점 방문처리 되어있는 곳 찾아보기
answer = 0
for x in range(size):
    for y in range(size):
        if graph[x][y] == 1:
            is_answer = True
            for step in steps:
                nx = x + step[0]
                ny = y + step[1]
                # 해당 위치가 만족하지 않으면, False & break
                if graph[nx][ny] == 0:
                    is_answer = False
                    break
            # 여기까지 왔을 때, True라면 만족하는 정사각형
            if is_answer:
                answer += 1

# 정답 출력
print(answer)
