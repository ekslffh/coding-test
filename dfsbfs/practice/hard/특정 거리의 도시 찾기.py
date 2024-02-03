# 도시의 정보가 주어졌을 때 최단거리가 k인 도시번호 출력하기 (없으면 -1리턴)
from collections import deque

answer = []

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X 입력받기
n, m, k, x = map(int, input().split())

# 연결 정보 저장할 그래프
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a -> b 단방향 간선
    graph[a].append(b)

# x부터 출발하여 최단거리가 k인 도시들 찾기 (BFS)

# 최단 거리 저장할 배열
d = [-1] * (n + 1)

def bfs(start):
    global k
    # 큐 활용
    q = deque()
    # 시작지점 넣기
    q.append(start)
    # 시작지점은 0
    d[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            # 방문하지 않았다면, 1. 큐에 넣기, 2. 이전값에 + 1
            if d[i] == -1:
                q.append(i)
                d[i] = d[now] + 1
                # 이때 거리가 k라면 answer에 추가해주기
                if d[i] == k:
                    answer.append(i)
    # 정답 오름차순 정렬
    answer.sort()

bfs(x)

if len(answer) == 0:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])
