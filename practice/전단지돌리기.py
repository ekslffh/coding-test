from collections import deque

INF = int(1e9)

# 전단지 돌리기 (다익스트라?)
# 노드개수, 시작점, 힘 입력받기
n, s, d = map(int, input().split())
# 결과값 저장하기
result = [INF] * (n + 1)
# 간선정보 저장할 리스트
graph = [[] for _ in range(n + 1)]
# 간선의 정보 (n-1)개 입력받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    # 양방향 : 거리는 모두 1
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = deque([start])
    result[start] = 0
    cnt = 0
    while q: # 큐가 빌때까지
        now = q.popleft()
        for i in graph[now]:
            if result[i] == INF:
                result[i] = result[now] + 1
                q.append(i)
    for i in range(1, n + 1):
        if i != start and result[i] >= d:
            cnt += 1
    answer = (cnt - 1) * 2
    print(answer)

dijkstra(s)
