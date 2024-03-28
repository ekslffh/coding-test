from collections import deque
import heapq

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key=lambda x: (-x[0]))
q = deque(data)

max_date = data[0][0]

answer = 0
result = []
for day in range(max_date, 0, -1):
    while q and q[0][0] >= day:
        val = q.popleft()
        heapq.heappush(result, -val[1])
    if result:
        answer += -heapq.heappop(result)

print(answer)
