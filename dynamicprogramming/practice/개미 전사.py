# dp 테이블
d = [0] * 100

n = int(input())

data = list(map(int, input().split()))

d[0] = data[1]
d[1] = max(data[0], data[1])
for x in range(2, n):
    d[x] = max(d[x - 1], d[x - 2] + data[x])

print(d[n - 1])
