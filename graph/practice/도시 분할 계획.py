# N개의 집과 M개의 길(양방향)로 이루어진 도시에서 모든 도시가 연결된 최소 신장트리 구하기 : 크루스칼 알고리즘

# 특정 집합의 루트 노드 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면, 재귀적으로 돌려서 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 개수 N, 길의 개수 M 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 생성

# 부모 테이블을 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 길의 정보 입력받기 a, b, c : a - b 연결하는 길의 유지비가 c
edges = []
result = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 비용을 기준으로 오름차순 정렬하기
edges.sort()

# 길의 정보 돌면서 가장 작은 비용부터 길 유지하기! 단, 사이클 발생시 무시
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생한다면 해당 길 무시하기
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    # 그렇지 않다면 합치고 result 배열에 추가하기
    else:
        union_parent(parent, a, b)
        result.append(cost)

# 결과적으로 최소신장트리를 구하였고 이중에서 가장 큰 유지비를 빼면서 두개의 마을로 나누면 정답
answer = sum(result) - max(result)

print(answer)
