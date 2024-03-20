import copy

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

dice = [0] * 6

# 동, 서, 북, 남
d = [[(0, 2), (2, 5), (3, 0), (5, 3)], [(0, 3), (2, 0), (3, 5), (5, 2)], [(0, 1), (1, 5), (4, 0), (5, 4)], [(0, 4), (1, 0), (4, 5), (5, 1)]]
steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]

answer = []
for order in orders:
    nx = x + steps[order - 1][0]
    ny = y + steps[order - 1][1]
    # 범위 검사
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    # 주사위 정보 갱신
    temp_dice = copy.copy(dice)
    for a, b in d[order - 1]:
        dice[b] = temp_dice[a]
     # 숫자 복사
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        # 복사하고 그래프 0
        graph[nx][ny] = 0
    # 여기서 상면은 인덱스 0, 하면은 인덱스 5
    answer.append(dice[0])

for i in answer:
    print(i)
