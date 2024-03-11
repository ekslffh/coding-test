# 빙고칸의 정보와 부르는 정보가 주어졌을 때, 3개의 빙고가 완성되는 지점의 순번 구하기

# 5 X 5 빙고판 정보 받기
n = 5
graph = []
for _ in range(n):
    # 1 ~ 25의 숫자가 들어감
    graph.append(list(map(int, input().split())))

# 불러주는 정보 입력
answer = []
for _ in range(n):
    answer.append(list(map(int, input().split())))

# 빙고가 되었는지 검사하기
def check_bingo():
    global n
    cnt = 0
    # 가로 검사
    for x in range(n):
        is_bingo = True
        for y in range(n):
            if graph[x][y] != 0:
                is_bingo = False
                break
        if is_bingo:
            cnt += 1
    # 세로 검사
    for y in range(n):
        is_bingo = True
        for x in range(n):
            if graph[x][y] != 0:
                is_bingo = False
                break
        if is_bingo:
            cnt += 1

    # 대각선 검사 X
    x, y = 0, 0
    is_bingo = True
    for i in range(n):
        nx = x + i
        ny = y + i
        if graph[nx][ny] != 0:
            is_bingo = False
            break
    if is_bingo:
        cnt += 1
    x, y = 4, 0
    is_bingo = True
    for i in range(n):
        nx = x - i
        ny = y + i
        if graph[nx][ny] != 0:
            is_bingo = False
            break
    if is_bingo:
        cnt += 1
    # cnt >= 3 이면, True
    if cnt >= 3:
        return True
    else:
        return False

# 특정 값 찾아서 체크하기
def find_pos(val):
    global n
    for x in range(n):
        for y in range(n):
            if graph[x][y] == val:
                graph[x][y] = 0
                return

result = 0
for i in range(n):
    for j in range(n):
        # 값 체크하기
        find_pos(answer[i][j])
        # 빙고 확인하기
        if check_bingo():
            result = (i * n) + j + 1
            break
    if result > 0:
        break

print(result)
