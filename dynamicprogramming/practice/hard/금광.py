# 테스트 횟수 입력
t = int(input())

# 좌상, 좌, 좌하 3가지 방향 (x, y)
steps = [(-1, -1), (0, -1), (1, -1)]

# t번 반복하면서 금의 최대 크기 출력
for _ in range(t):
    # 행과 열 입력
    n, m = map(int, input().split())
    # 금광 정보 입력
    input_data = list(map(int, input().split()))
    # 행, 열로 나누어서 그래프에 저장
    graph = []
    for i in range(n):
        idx = i * m
        graph.append(input_data[idx:idx + m])
    # 금 개수 답을 변수
    answer = -1
    # DP 테이블
    d = [[-1] * m for _ in range(n)]
    # 첫 열은 현재 값으로 넣어주기
    for i in range(n):
        d[i][0] = graph[i][0]
    # 두 번째 열부터 최선의 값 구해보기
    for y in range(1, m):
        for x in range(n):
            # 현재 행을 기준으로 이전의 3가지 경우 따져보기 현재 좌표 : (x, y)
            max_prev = -1
            for dx, dy in steps:
                nx = x + dx
                ny = y + dy
                # 범위를 벗어나면 나가기
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 벗어나지 않는다면 해당 값 중에서 최댓값 구해보기
                max_prev = max(max_prev, d[nx][ny])
            # 여기까지 온다면 현재 위치에서 최선의 이전 값을 구했으므로 현재 금과 합쳐서 갱신해주기
            d[x][y] = max_prev + graph[x][y]
            answer = max(answer, d[x][y])
    print(answer)
