# N개의 행성을 모두 연결하는데 필요한 최소 비용 구하기
# 중요한 점은, x, y, z 좌표들을 정렬하여서 간선의 개수를 줄이는 것이 핵심!!

# 특정 원소에 대한 집합 찾기
def find_parent(parent, x):
    # 부모 요소가 아니라면, 재귀 돌리기
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

# 행성의 개수 N 입력받기
n = int(input())
parent = [0] * n # 부모테이블 초기화

# 부모테이블을 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# 우선 모든 통로 정보 저장할 배열
edges = []
# 결과 변수
result = 0

# 모든 행성을 돌면서 통로 정보 넣어주기 N * N
# 0 ~ N - 1번의 행성 번호 부여
x_arr = []
y_arr = []
z_arr = []

# N개의 행성 좌표 입력받기 (x, y, z 좌표)
for i in range(n):
    x, y, z = map(int, input().split())
    x_arr.append((x, i))
    y_arr.append((y, i))
    z_arr.append((z, i))

# 각각 정렬해주기
x_arr.sort()
y_arr.sort()
z_arr.sort()

# 이제 각각의 좌표를 기준으로 간선추가해보기??
for i in range(n - 1):
    # (좌표, 행성번호(0~n-1))
    # 간선정보로 추가하기 (비용, 행성번호1, 행성번호2)
    edges.append((x_arr[i + 1][0] - x_arr[i][0], x_arr[i][1], x_arr[i + 1][1]))
    edges.append((y_arr[i + 1][0] - y_arr[i][0], y_arr[i][1], y_arr[i + 1][1]))
    edges.append((z_arr[i + 1][0] - z_arr[i][0], z_arr[i][1], z_arr[i + 1][1]))


# 비용을 기준으로 오름차순 정렬 : 이후에 낮은 비용부터 건설해볼 거임.
edges.sort()

for edge in edges:
    # 비용, a행성, b행성 번호
    cost, a, b = edge
    # 사이클이 발생하지 않았다면 연결하고 비용 더해주기
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 정답 출력
print(result)
