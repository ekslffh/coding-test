import sys
n = int(sys.stdin.readline())
time = []

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

# [[5, 20], [1, 16], [8, 14], [3, 5]]
time.sort(key = lambda x: x[1], reverse = True)

# 가장 늦은 시간에 해도 되는 일이 최소 시작해야 하는 시간
ans = time[0][1] - time[0][0]

# 시작해야 하는 시간만을 비교
for i in range(1, n):
    if ans > time[i][1]:
        ans = time[i][1] - time[i][0]
    else:
        ans -= time[i][0]

print(ans) if ans >= 0 else print(-1)
