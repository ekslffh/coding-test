# N개의 여행지에 대하여 양방향 도로 정보가 주어졌을 때, 여행계획이 가능한지 여부를 판별하기

# 도롱 정보에 따라서 합치고 주어진 여행지들이 한 집합안에 존재하는지 여부 판단하기

# 특정 원소에 대한 루트 노드 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 재귀적으로 돌리기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 하나로 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 개수 N, 여행계획에 속한 도시의 개수 M 입력
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모테이블 생성

# 부모테이블을 자기 자신으로 초기화 하기
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            parent[a] = b

# N개의 줄에 걸쳐서 두 여행지의 연결 정보 입력 (N X N 행렬)
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# 연결정보에 따라 두 도시를 연결하는 연산 수행
for a in range(n):
    for b in range(n):
        # 만약 연결되어 있다면, 합치기 연산 수행
        if graph[a][b] == 1:
            union_parent(parent, a + 1, b + 1)

# 여행계획에 포함된 M개의 여행지 정보 입력
plans = list(map(int, input().split()))
# 여행계획이 가능하면 YES, 불가능하면 NO 출력하기
answer= True

# 돌면서 같은 집합에 있는지 파악하기
for i in range(m - 1):
    # 같은 집합에 속해있지 않으면 실패 : 반복문 나가기
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i + 1]):
        answer = False
        break

# 계획이 가능하다면 YES 출력
if answer:
    print("YES")
# 불가능하다면, NO 출력
else:
    print("NO")
