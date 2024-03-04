# 1번 회사에서 K번 회사를 방문하고 X번 회사로 가는 최단 경로 구하기
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 회사의 개수 N, 경로의 개수 M 입력받기
n, m = map(int, input().split())
# 회사간의 연결 정보(M개) 입력받기 (양방향)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    # A, B 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# 현재위치 -> 현재위치는 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 최종 방문지 X, 소개팅 장소 K 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for t in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

# 1 -> K -> X 최단 경로 출력하기
answer = graph[1][k] + graph[k][x]
# 도달할 수 없다면 -1 출력
if answer >= INF:
    print(-1)
# 도달할 수 있다면 시간 출력
else:
    print(answer)
