# 1 -> k -> x
# 플로이드워셜 방식으로 구하기
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드와 간선의 개수 입력받기
n, m = map(int, input().split())
# 거리정보 저장할 2차원 리스트
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 k와 도착지 x 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)
