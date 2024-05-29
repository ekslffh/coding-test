# https://www.acmicpc.net/problem/2133

# 3 X N 벽을 2 X 1 & 1 X 2 타일로 채우는 경우의 수 구하기
# n이 2인 경우에는 3가지 이며, 4일 때는 a2 * 3 + 2

n = int(input())

dp = [0] * 31
dp[2] = 3

for x in range(4, n + 1):
    if x % 2 == 0:
        dp[x] = (dp[x - 2] * 3) + sum(dp[:x - 2]) * 2 + 2

print(dp[n])
