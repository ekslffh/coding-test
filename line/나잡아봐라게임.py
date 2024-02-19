# 코니, 브라운의 위치 입력받기
from collections import deque

c, b = map(int, input().split())

answer = []

q = deque()
q.append((c, b, 0))
result = -1

while q:
    cony, brown, second = q.popleft()
    if not 0 <= cony <= 200000 or not 0 <= brown <= 200000:
        continue
    if cony == brown:
        result = second
        break
    else:
        q.append((cony + second + 1, brown - 1, second + 1))
        q.append((cony + second + 1, brown + 1, second + 1))
        q.append((cony + second + 1, brown * 2, second + 1))

print(result)
