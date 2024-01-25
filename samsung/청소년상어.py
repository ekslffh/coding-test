# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
import copy

# 물고기 정보 넣을 그래프
board = [[] for _ in range(4)]

for j in range(4):
    input_data = list(map(int, input().split()))
    # 입력받아서 (물고기번호, 방향) 형식으로 그래프에 저장하기 (방향은 zero-base로 변경)
    row = []
    for i in range(0, len(input_data), 2):
        row.append([input_data[i], input_data[i + 1] - 1])
    board[j] = row

# 방향 정의하기 (위에서부터 반시계로 총 8방향) x: 행, y: 열 => (x, y) 형태로 저장
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]
        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + direction[nd][0]
            ny = f_y + direction[nd][1]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    ds = board[sx][sy][1]

    for i in range(1, 4):
        px = sx + direction[ds][0] * i
        py = sy + direction[ds][1] * i
        if (0 <= px < 4 and 0 <= py < 4) and board[px][py][0] > 0:
            dfs(px, py, score, copy.deepcopy(board))

# 초기 세팅
# 물고기 합 구할 결과 변수
dfs(0, 0, 0, board)
print(max_score)
