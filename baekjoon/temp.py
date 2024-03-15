from collections import deque

q = deque([1,2,3,4])

while q:
    print(q.popleft())

a = [5,6,7,8]
q = deque(a)

print(q)
print(q.popleft())
