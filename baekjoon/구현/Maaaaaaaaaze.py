import sys
from collections import deque
from itertools import permutations

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
b = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

dh = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)

def rotate(b):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4 - i] = b[i][j]
    return tmp

# 이제 정해진 경우에 따른, 최소 경로값 구해보기
def bfs(b):
    global result
    q = deque()
    # 거리를 저장할 배열 선언
    dist = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    # 시작 위치는 0층 0행, 0열
    q.append((0, 0, 0))
    while q: # 큐가 빌때까지
        h, y, x = q.popleft()
        # 마지막까지 도달한 경우에는 결과값 비교해서 갱신하기
        if (h, y, x) == (4, 4, 4):
            result = min(result, dist[4][4][4])
            # 최단 경로는 12이면 더이상 검사안함
            if result == 12:
                print(result)
                exit()
            return
        # 3차원이므로 x, y, z 축을 위아래로 움직여보기
        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 검사
            if nh < 0 or nh >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            # 해당 위치에 갈 수 없거나, 이미 갔거나 하면 continue
            elif b[nh][ny][nx] == 0 or dist[nh][ny][nx] != 0:
                continue
            # 모든 조건을 통과하면, 해당 값 큐에 넣어주기
            q.append((nh, ny, nx))
            # 거리배열 데이터 저장해주기
            dist[nh][ny][nx] = dist[h][y][x] + 1

# 현재 순서가 정해져있는 판을 각각 회전해보면서 경우의 수 만들기
def dfs(d):
    global b
    # 마지막까지 도달했을 경우, bfs 탐색 수행
    if d == 5:
        if b[4][4][4]:
            bfs(b)
        return
    # 총 4번 회전시켜보면서 재귀 돌리기
    for i in range(4):
        b[d] = rotate(b[d])
        if b[0][0][0]:
            dfs(d + 1)

def solve():
    # 0 ~ 4까지의 판을 순열조합으로 만들어서 검사하기
    for d in permutations([0, 1, 2, 3, 4]):
        for i in range(5):
            b[i] = board[d[i]]
        dfs(0)

solve()

if result == sys.maxsize:
    result = -1
print(result)
