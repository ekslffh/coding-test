n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

# 로프를 오름차순 정렬시키기.
ropes.sort()
# 작은 로프부터 최대 중량 구해서 비교하기.
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (n - i))

print(max_weight)
