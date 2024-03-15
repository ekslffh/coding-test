# 감시 : 사각지대의 최소크기 구하기
import copy

n, m = map(int, input().split())
graph = []
cctvs = []
empty_cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            # (x, y, 종류)
            cctvs.append((i, j, graph[i][j]))
        elif graph[i][j] == 0:
            empty_cnt += 1

# cctv 종류별(1 ~ 4), 방향별 감시 범위 정의 (동, 남, 서, 북) (x, y)
d = [
        [],
        [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]], # 1번 cctv
        [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]], # 2번
        [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]], # 3번
        [[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(0, -1), (0, 1), (1, 0)], [(-1, 0), (1, 0), (0, -1)]], # 4번
        [[(0, 1), (1, 0), (0, -1), (-1, 0)]] # 5번
    ]

# 정해진 이동경로에 따라 움직이면서 사각지대 개수 리턴하기
def monitor(d_arr):
    result = 0
    global n, m, graph
    temp_graph = copy.deepcopy(graph)
    for i in range(len(cctvs)):
        x, y, c = cctvs[i]
        for dx, dy in d[c][d_arr[i]]:
            cnt = 1
            while True:
                nx = x + (dx * cnt)
                ny = y + (dy * cnt)
                cnt += 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m or temp_graph[nx][ny] == 6:
                    break
                elif 1 <= temp_graph[nx][ny] <= 5:
                    continue
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 8
                    result += 1
    return result

# cctv들 종류에 따라 회전 시켜주기
def turn_cctv(n, d_arr, answer):
    # 모든 cctv에 대한 방향이 지정되었다면 모니터링 진행
    if n == len(cctvs):
        answer.append(monitor(d_arr))
    else:
        # n번째 cctv에 대한 x, y, 종류
        x, y, c = cctvs[n]
        for i in range(len(d[c])):
            # n번째 cctv에 대하여 i번째 이동경로를 설정
            da = copy.copy(d_arr)
            da.append(i)
            turn_cctv(n + 1, da, answer)

answer = []
turn_cctv(0, [], answer)

answer = empty_cnt - max(answer)

print(answer)
