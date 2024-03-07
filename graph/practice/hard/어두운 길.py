# N개의 집과 M개의 도로가 주어졌을 때, 최소신장 트리 구하기
# 절약할 수 있는 최대 금액을 구하기 위해서는 유지할 수 있는 최소 금액을 구하면 된다.

# 특정 원소의 집합 구하기
def find_parent(parent, x):
    # 부모 요소가 아니라면, 찾을 때까지 재귀 함수 돌리기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소의 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 수 N, 도로의 수 M 입력받기
n, m = map(int, input().split())
parent = [0] * n # 부모 정보 저장할 배열

# 우선 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# 도로 정보 저장할 배열
edges = []
# 기존의 유지비
cur_cost = 0
# 절약한 이후의 유지비
save_cost = 0
# m개의 도로 정보 입력받기
for _ in range(m):
    # x, y를 잇는 도로의 길이(비용)은 z라는 의미
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    # 전체 비용 미리 계산하기
    cur_cost += z

# 비용을 기준으로 오름차순 정렬
edges.sort()

# 크루스칼 알고리즘을 활용하여 최소 신장 트리 구하기
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생한다면 (이미 연결되어 있다면), 스킵하기
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    # 그게 아니라면 연결해주고 비용 save_cost에 저장해주기
    else:
        union_parent(parent, a, b)
        save_cost += cost

# 최대 금액 = 전체 금액 - 최소 신장 트리 금액
answer = cur_cost - save_cost

# 정답 출력
print(answer)
