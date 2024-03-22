from copy import copy

a = [(0, 0) for _ in range(6)]
print(a)
b = copy(a)
b[0] = (1, 9)
print(b)
print(b.count((0, 0)))

