# 도시를 두개로 분할하고 그 안에서의 길들을 최소한의 비용으로 유지하고 싶다.
# 최소 신장 트리

# 부모찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 재귀함수로 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 간선정보 저장할 리스트
edges = []
# 각 노드의 부모 저장할 배열
parent = [0] * (n + 1)

# 부모를 자기자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a와 b를 잇는 길의 유지비가 c이다.
    edges.append((c, a, b))

# 비용을 기준으로 오름차순 정렬
edges.sort()

# 최소 유지비 저장할 변수
result = 0
max_cost = 0

# 비용이 작은 순으로 간선정보 돌면서 cycle이 발생하지 않는다면 길유지하기
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 최소유지비에 더해주기
        result += cost
        # 가장 큰 비용 찾기
        max_cost = max(max_cost, cost)

# 도시를 분할하므로 가장 비용이 큰 길을 기준으로 나눌것.
result -= max_cost
print(result)
