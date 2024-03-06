# 0 ~ N번까지의 번호를 부여하고 '팀 합치기', '같은 팀 여부 확인' 연산 수행하기

# 같은 팀 여부 확인 (루트 노드 찾기)
def find_parent(parent, x):
    # 루트 노드가 아니라면 찾을 때 까지 재귀 돌리기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 생성

# 루트를 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    # 연산종류, 팀a, 팀b 입력받기
    option, a, b = map(int, input().split())
    # 팀 합치기 연산 수행
    if option == 0:
        union_parent(parent, a, b)
    # 같은 팀 여부 확인해서 맞으면 'yes', 틀리면 'no' 출력
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
