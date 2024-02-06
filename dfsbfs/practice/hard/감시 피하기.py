# N x N 복도가 있고, 학생과 선생님의 위치정보가 주어진다.
# 선생님은 장애물을 있는 넘어는 보지못하고 그렇지 않으면 상하좌우로 감시가능
# 여기서 학생들은 장애물을 3개를 설치해서 안걸리도록 해야한다.
import sys
from itertools import combinations
import copy

# 복도의 크기(n) 입력받기
n = int(input())
# 복도의 정보 입력받기
graph = []
for _ in range(n):
    data = list(input().split())
    graph.append(data)
# 복도의 정보 돌면 빈칸인 부분 정보 얻기 (이 중 3곳을 장애물 세울겨)
empty_space_info = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            empty_space_info.append((i, j)) # (행, 열)

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 선생님한테 걸리는지 확인하는 함수, 걸리면 True 리턴, 안걸리면 False 리턴
# 전체 맵을 돌면서 선생님이면 상하좌우로 이동해보면서 걸리는지 확인해보기
def check_find(graph):
    global n
    # 현재 선생님의 위치가 (x, y)
    # 이를 기준으로 상하좌우 이동해보기 (4방향)
    for x in range(n):
        for y in range(n):
            # 선생님이면 상하좌우로 이동해보기
            if graph[x][y] == 'T':
                for i in range(4):
                    cnt = 1
                    while True:
                        nx = x + (dx[i] * cnt)
                        ny = y + (dy[i] * cnt)
                        # 범위를 벗어나거나 장애물을 만나면 종료
                        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 'O':
                            break
                        # 학생이라면 걸린 것이기 때문에 바로 True 리턴하기
                        elif graph[nx][ny] == 'S':
                            return True
                        # 아닌 경우(빈곳이거나 다른 선생님 존재)는 cnt를 올려서 한층 더 위로 갈 수 있도록 한다.
                        else:
                            cnt += 1
    # 모든 경우를 다 겪었을 때, 문제없으면 안걸린 것 : False 리턴
    return False

# 위의 정보들 중에서 순서 상관없이 3개씩 고르는 경우 구하기 (combinations)
rnd_space_comb = list(combinations(empty_space_info, 3))
# 경우들 돌면서 그곳에 장애물 세워놓고 선생님한테 안걸리는지 확인해보기
for rsc in rnd_space_comb:
    temp_graph = copy.deepcopy(graph)
    # 3개의 (행, 열)정보 돌면서 장애물 설치하기
    for x, y in rsc:
        temp_graph[x][y] = 'O'
    # 임시로 장애물을 설치해보고 선생님한테 걸리는지 검사해보기

    # 결과가 True라면?, 즉 걸렸다면? 다음 배치로 다시 도전해보기
    # 결과가 False라면?, 즉, 안걸리고 성공했다면 그대로 YES리턴하고 시스템 종료하기
    if not check_find(temp_graph):
        print("YES")
        sys.exit()

# 전체를 다 돌고도 가능한 경우가 없었다면 "NO" 출력하기
print("NO")
