# 가장 비싼 보석부터, 작은 무게의 가방부터
import heapq
import copy

# 보석의 개수 N, 가방의 개수 K 입력
n, k = map(int, input().split())
# 보석과 가방 정보 입력
jewels = []
for _ in range(n):
    # 무게 m, 가격 v
    jewels.append(list(map(int, input().split())))
bags = []
for _ in range(k):
    # 수용 가능 무게 입력
    bags.append(int(input()))

jewels.sort()
# 가방을 무게 기준 오름차순 정렬
bags.sort()

tmp = []
answer = 0
for bag in bags: # 각 가방 무게에 대해
    while jewels and jewels[0][0] <= bag: #제일 가벼운 보석무게를 bag이 허용하는한 반복
        heapq.heappush(tmp, -jewels[0][1]) # 가격을 최대힙에 저장(음수로 저장하여 최소힙을 최대힙으로)
        heapq.heappop(jewels) # 가격 저장한 보석은 버리기
    if tmp: #bag 무게 이하 보석 가격 다 저장했으면
        answer -= heapq.heappop(tmp) # 제일 가치가 높은 가격 더하기(음수니까 빼기)
print(answer)
