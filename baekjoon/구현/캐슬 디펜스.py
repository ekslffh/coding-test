from itertools import combinations
import copy

# 행, 열, 공격 제한 거리 입력
n, m, d = map(int, input().split())

# 맵 정보 입력
graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    # 바로 적 개수 세보기
    for x in graph[i]:
        if x == 1:
            cnt += 1

# 궁수 배열 추가 (처음에는 비어있음.)
graph.append([0] * m)

# 궁수는 0 ~ (m - 1)번 중에 3곳씩 배치 가능
cases = list(combinations([x for x in range(m)], 3))

# 특정 궁수에 가장 가까운 적 찾기
def find_target(px, py, game_graph):
    global n, m, d
    # 거리는 최대거리로 설정
    min_d = 1e9
    result = []
    for x in range(n):
        for y in range(m):
            if game_graph[x][y] == 1:
                cur_d = abs(px - x) + abs(py - y)
                # 더 작은 거리가 있으면 result 갱신
                if min_d > cur_d:
                    min_d = cur_d
                    result = [(x, y)]
                # 같은 거리 좌표가 있다면, result에 추가
                elif min_d == cur_d:
                    result.append((x, y))
    # 만약 reulst에 요소가 여러개 있을 수도 있기 때문에, 가장 왼쪽에 있는 녀석을 붙여주기
    # 그 말은, y기준 오름차순 정렬하기
    result.sort(key= lambda x: x[1])
    # 공격 제한 거리 로직 추가
    if len(result) == 0 or min_d > d:
        return (-1, -1)
    return result[0]

# 배치된 데이터를 기준으로 게임 진행
def play_game(game_graph):
    global n, m, d, cnt
    # 모든 적이 게임에서 제외될 때까지 반복 수행
    answer = 0
    cur_cnt = cnt
    while cur_cnt > 0:
        # 각 궁수는 가장 가까운 거리에 왼쪽 적을 공격한다.
        temp_result = []
        for i in range(m):
            if game_graph[n][i] == 2:
                tx, ty = find_target(n, i, game_graph)
                # 공격 가능 적이 있따면, 공격하고 게임에서 제외
                if tx != -1 and ty != -1:
                    # 같은 적이 타겟이 될 수 있기에 바로 지우지 말고 동시 공격이 끝난 이후에 지워주기
                    temp_result.append((tx, ty))
                    # game_graph[tx][ty] = 0
                    # answer += 1
                    # cur_cnt -= 1
                    if cur_cnt <= 0:
                        return answer
        # 여기서 화살 맞은 적 다 제거하기
        for x, y in set(temp_result):
            # 아직 한번도 화살 처리가 안된 적에 대해서만
            game_graph[x][y] = 0
            answer += 1
            cur_cnt -= 1
            if cur_cnt <= 0:
                return answer
        # 적은 아래로 한칸씩 이동한다.
        temp_graph = [[0] * m for _ in range(n)]
        for x in range(n + 1):
            # 궁수는 그대로
            if x == n:
                temp_graph.append(copy.copy(game_graph[n]))
                continue
            for y in range(m):
                if game_graph[x][y] == 1:
                    nx, ny = x + 1, y
                    # 범위를 벗어나면 pass
                    if nx >= n:
                        cur_cnt -= 1
                        continue
                    # 아래로 이동 시켜주기
                    temp_graph[nx][ny] = 1
        game_graph = temp_graph
    # 죽인 적의 수 리턴
    return answer

answer = 0
# 각 케이스마다 궁수를 배치하고 값 구해보기
for case in cases:
    temp_graph = copy.deepcopy(graph)
    # 각 케이스마다 궁수 위치 변경
    for i in range(m):
        if i in case:
            temp_graph[n][i] = 2
    answer = max(answer, play_game(temp_graph))

print(answer)
