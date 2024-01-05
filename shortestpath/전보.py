import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 도시의 개수, 통로의 개수, 도시 c 입력받기
n, m, c = map(int, input().split())
# 각 도시별 연결 정보 담을 그래프
graph = [[] for _ in range(n + 1)]
# 거리정보 담을 리스트
times = [INF] * (n + 1)

# 연결정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # 도시 x에서 도시 y로 메시지 보내는데 걸리는 시간은 z (단방향)
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    times[start] = 0
    heapq.heappush(q, (0, start))
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        t, now = heapq.heappop(q)
        # 이미 거쳐간 도시는 패스 (중복방문x)
        if times[now] < t:
            continue
        # 연결된 통로정보에 따라서 반복
        for i in graph[now]:
            cost = t + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if times[i[0]] > cost:
                times[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c)

# 도달할 수 있는 도시의 개수
city_num = 0
# 도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단 거리
max_time = 0
for i in range(1, n + 1):
    # 갈수없거나 자기자신이거나하면 continue
    if times[i] == INF or i == c:
        continue
    else:
        city_num += 1
        max_time = max(max_time, times[i])

print(city_num, max_time)
