# 단방향 통로가 존재하고 핻강 통로를 통해서 전보를 보낼 수 있고, 일정 시간이 소요된다.
# C에서 최대한 많이 메시지를 보내려고 할때, 메시지를 받을 수 있는 도시와 걸리는 시간 출력

# 다익스트라 알고리즘을 통해서 C에서 각 도시에 대한 시간을 계산하고 보낼 수 있는 도시들 중 최대 시간을 구하면 된다.
import heapq

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
# 도시의 개수 N, 통로의 개수 M, 보내고자 하는 도시 C 입력받기
n, m ,c = map(int, input().split())
# 걸리는 시간 담을 배열 선언 (INF로 초기화)
distance = [INF] * (n + 1)
# 연결정보 저장할 배열
graph = [[] for _ in range(n + 1)]
# 통로 정보 입력받기
for _ in range(m):
    # X, Y, Z 입력받기 => X에서 Y로 보내는 데 걸리는 시간이 C이다. (단방향)
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 최소힙에 시작 값 넣어주기
    heapq.heappush(q, (0, start))
    # 시작거리 0으로 초기화
    distance[start] = 0
    while q: # q가 비지 않을 때까지 반복
        # 걸리는 시간, 최소값 꺼내오기
        dist, now = heapq.heappop(q)
        # 이미 처리된 적이 있는지 검사
        if distance[now] < dist:
            continue
        # 현재 노드 기준 통로 정보 가져오기
        for i in graph[now]:
            # 현재 노드를 거쳐서 가는 시간 계산해보기
            cost = dist + i[1]
            # 비용이 기존의 시간보다 적다면 갱신해주고 최소힙에 넣어주기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

# 메시지를 받는 도시의 개수와 총 걸리는 시간 출력하기
cnt = 0
tm = 0
for i in range(1, n + 1):
    if distance[i] != INF:
       cnt += 1
       tm = max(tm, distance[i])

# 자기 자신 빼고 출력
print(cnt - 1, tm)
