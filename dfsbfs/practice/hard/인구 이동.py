# 인구이동이 몇일동안 일어나는지 출력하기

# n x n 크기의 땅이 있고 두 나라의 인구차이가 L이상 R이하라면 국경선을 열어야 한다.
n, l, r = map(int, input().split())
# n개의 줄에 땅의 정보 입력받기 (각 칸의 인구수)
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 이동값 (x, y)
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 맵을 돌면서 인구차이가 L이상 R이하라면 국경선 열기 (recursion?)
def recursion(x, y, union, visited):
    # [x][y]에 대하여 상하좌우로 국경선 파악해보기
    global n, l, r
    # 방문처리
    visited[x][y] = True
    # 상하좌우 이동해보기
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        # 범위를 벗어나거나 방문했었는지 검사하기
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            continue
        # 현재 값과 비교해서 L이상 R이하인지 검사하고 맞으면 연합에 추가하기
        comp_val = abs(graph[x][y] - graph[nx][ny])
        if l <= comp_val <= r:
            union.append((nx, ny))
            # 다시 그 나라 기준으로 재귀 돌려보기
            recursion(nx, ny, union, visited)

# 열려있는 나라들끼리 연합을 맺고 인구이동을 시작한다. 모든 인원수 // 칸의 개수로 인구 배정
# 날짜를 셀 변수 선언
answer = 0
while True:
    # 연합들 저장할 변수
    unions = []
    # 하루기준으로 방문처리 하면서 연합 세보기
    visited = [[False] * n for _ in range(n)]
    # 모든 칸에 대해서 연합 만들어보기
    for x in range(n):
        for y in range(n):
            # 아직 방문하지 않은 곳이 있다면 그 곳을 중심으로 연합만들어보기
            if not visited[x][y]:
                union = [(x, y)]
                recursion(x, y, union, visited)
                # 여기까지 끝났을 때, 한 연합에 대한 정보가 다 들어와 있을 것이다. 이를 unions에 저장해두자
                # 예외경우 ) 만약에 상하좌우로 넣을게 없어서 x,y 하나만 들어있는 경우는 인구이동 안일어남
                if len(union) > 1:
                    unions.append(union)
    # 여기까지 왔을 때, unions가 비어있는 경우, 게임 종료 -> 인구이동이 안일어났다는 의미이다.
    if len(unions) == 0:
        break
    # 아니라면 인구이동이 필요한 경우 : 연합들 돌면서 특정 연합에 대한 평균값으로 그래프정보 갱신해주기
    else:
        for union in unions:
            # 넣어줄 값은 전체 평균값이다.
            sum = 0
            for x, y in union:
                sum += graph[x][y]
            avg = sum // len(union)
            for x, y in union:
                graph[x][y] = avg
        # 인구이동이 필요했으므로 하루 추가해주기
        answer += 1

# 정답 출력
print(answer)
