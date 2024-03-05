# 1 ~ N번까지의 헛간 중에서 1번 헛간으로부터 최단 거리가 가장 먼 헛간의 번호를 출력하기
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
# 헛간의 개수 N, 양방향 통로의 개수 M 입력받기
n, m = map(int, input().split())
# 연결 정보 담을 배열 생성
graph = [[] for _ in range(n + 1)]
# M개의 통로 정보 입력받기
for _ in range(m):
    # a와 b는 연결되어 있다는 의미 (양방향)
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 최단 거리 담을 배열 무한으로 초기화
distance = [INF] * (n + 1)

def dijkstra(start):
    # 시작은 1번 헛간부터
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 빌 때까지
        # 거리가 가장 작은 값부터 가져오기 (최소힙)
        dist, now = heapq.heappop(q)
        # 이미 처리한 적이 있는지 검사하기
        if distance[now] < dist:
            continue
        # now와 연결되어 있는 원소들 찾기
        for i in graph[now]:
            # 비용 구하기
            cost = dist + 1
            # 연결되어 있는 헛간 i에 대하여 기존의 값과 비교해보기
            if cost < distance[i]:
                # 갱신해주고 최소힙에 넣어주기 (거리, 헛간)
                distance[i] = cost
                heapq.heappush(q, (cost, i))

# 1번 통로에 대한 최단거리 구하기 (다익스트라 알고리즘)
dijkstra(1)

# 가장 먼 거리 구하기
max_distance = -1
for i in range(1, n + 1):
    if distance[i] != INF and max_distance < distance[i]:
        max_distance = distance[i]

# 정답을 담을 배열 선언
answer = []
for i in range(1, n + 1):
    if distance[i] == max_distance:
        answer.append(i)

# 헛간번호, 거리, 같은 거리 헛간의 개수 순으로 출력하기
print(min(answer), max_distance, len(answer))
