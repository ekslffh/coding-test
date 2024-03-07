# G개의 탑승구가 있고, P개의 비행기를 도킹할 때, 어떠한 탑승구에도 도킹하지 않은 비행기가 나오면, 공항의 운행을 중지한다.
# 최대로 도킹할 수 있는 비행기의 개수 출력
# 단, 한 탑승구에는 하나의 비행기만 도킹이 가능하다.

# 탑승구의 수 G 입력받기
g = int(input())
# 비행기의 수 P 입력받기
p = int(input())
# 각 비행기가 도킹할 수 있는 탑승구의 정보 입력받기
infos = [[] for _ in range(p)]
for i in range(p):
    infos[i] = [x for x in range(1, int(input()) + 1)]
# 도킹 가능한 비행기의 최대 개수 출력하기
answer = 1
for i in range(p):
    # 젤 끝의 원소 (가장 큰 숫자) 꺼내고 다른 비행기에서도 가능 원소에서 제거해보기
    now = infos[i].pop()
    # 이후에 비행기 돌면서 해당 숫자 제거하기
    for j in range(i + 1, p):
        if now in infos[j]:
            infos[j].remove(now)
            # 세울 수 있는 곳이 없는지 검사
            # 없다면 j번까지가 가능했던 지점
            if len(infos[j]) == 0:
                answer = j
    if answer != 1:
        break

print(answer)
