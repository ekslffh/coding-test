# A에서 B로 가는 비용의 최솟값 구하기
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
# 도시의 개수 N 입력
n = int(input())
# 버스의 개수 M 입력
m = int(input())
# 버스의 정보 입력
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    # a -> b의 비용이 c
    a, b, c = map(int, input().split())
    # 같은 곳을 가는 버스의 경우, 최소 비용이 걸리는 버스로 설정하기
    graph[a][b] = min(graph[a][b], c)
# 자기 자신에 대하여 거리는 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 전체 정보 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 갈 수 없으면 0 출력하기
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
