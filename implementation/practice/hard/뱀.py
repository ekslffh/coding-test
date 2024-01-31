# N * N 보드크기에 뱀이 이동한다.
# 처음 0,0에서 오른쪽으로 출발한다.
# 사과를 먹게 되면 몸길이가 늘어난다.
# 중간에 X초 후에 방향을 이동하는 정보가 주어진다.
# 방향을 이동하고 움직였을 때, 머리가 자신의 몸과 닿거나, 벽이면 게임 종료

# 모든 보드의 값은 0이고 사과있는 곳은 1이고 뱀이 위치하면 2
# 보드의 크기 N 입력받기
n = int(input())
board = [[0] * n for _ in range(n)]
# 사과의 개수 K 입력받기
k = int(input())
# K번 사과의 위치 (행, 열)로 입력받아서 보드에 저장하기 (저장할 때 행-1, 열-1로 저장)
for _ in range(k):
    row, col = map(int, input().split())
    # 0,0부터 시작하므로 1씩 빼서 저장해주기 : 1행 1열은 (0,0)
    board[row - 1][col - 1] = 1
# 뱀의 방향 변환 횟수 L 입력받기
l = int(input())
# L번 X(초), C(방향: D or L) 입력받아서 저장해놓기 (map으로 저장해서 바로 찾아내기)
turn_info_map = {}
for _ in range(l):
    # x초 후에 c로 회전한다. c가 D이면 오른쪽, L이면 왼쪽
    x, c = input().split()
    turn_info_map[int(x)] = c

# 방향정보 저장하고 turn함수 정의해놓기 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 방향은 d이고 c에 따라 회전하고 방향 리턴하기
def turn(d, c):
    # 오른쪽 회전일 경우
    if c == 'D':
        d += 1
        if d > 3:
            d = 0
    # 왼쪽 회전일 경우
    else:
        d -= 1
        if d < 0:
            d = 3
    return d

# 반복문 전에 정의해야 할 변수 (뱀의 위치는 좌상단 ,초(정답), 꼬리정보)
board[0][0] = 2
# 뱀이 보드에 위치하고 있는 정보 머리 - 몸통 - 꼬리 순으로 정리하기
snake_info = [(0,0)]
# 방향은 동쪽(0)부터 시작
d = 0
# 계산할 초
second = 0
# 방향대로 한번 가보고 벽이거나 자기랑 부딪히면 게임종료, 사과가 있으면 먹고 없으면 꼬리 없애고, x초후에 turn정보 있는지 확인해서 처리해주기
while True:
    second += 1
    # 여기서 회전 정보 있는지 검사해보기
    x, y = snake_info[0]
    nx = x + dx[d]
    ny = y + dy[d]
    # 이동한 곳이 벽이거나 내 몸이 있다면 게임종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break
    elif board[nx][ny] == 2:
        break

    # 사과가 없으면 True
    is_apple = board[nx][ny] != 1

    # 그렇지 않다면 이동은 해본다.
    snake_info.insert(0, (nx, ny))
    # 뱀위치들어있는거를 표시해주기
    board[nx][ny] = 2
    # 이제 사과가 있는지 확인해서 꼬리를 당길지 둘지를 결정해야 한다.
    if is_apple:
        # 사과가 없다면 꼬리를 땡기고 그 다음 정보가 꼬리가 되는 것이다.
        # 마지막 녀석 삭제해주기
        x, y = snake_info.pop()
        # 보드에서 정보 지워주기
        board[x][y] = (0,0)
    # 여기까지 이동이 성공적으로 된다음에 회전할지 말지를 검사한다.
    if second in turn_info_map:
        # 만약 해당 초에 회전 정보가 있다면 turn함수를 이용하여 회전하기
        d = turn(d, turn_info_map[second])

print(second)
