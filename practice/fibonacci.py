# 다이나믹 프로그래밍을 이용해서 반복되는 연산을 저장하자
n = int(input())
result = []
arr = []

# dp테이블
d = [(0, 0) for _ in range(41)]
d[0] = (1, 0)
d[1] = (0, 1)

for i in range(2, 41):
    z = d[i - 1][0] + d[i - 2][0]
    o = d[i - 1][1] + d[i - 2][1]
    d[i] = (z, o)

for i in range(n):
    arr.append(int(input()))

for a in arr:
    print(d[a][0], d[a][1])
