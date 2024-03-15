from copy import copy

n = int(input())
hp = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = []
arr = []
for i in range(n):
    # 현재 인덱스는 사용불가
    if hp[i] >= 100:
        continue
    arr.append((hp[i], joy[i]))
    for t_hp, t_joy in dp:
        # (체력, 기쁨)
        if t_hp + hp[i] < 100:
            arr.append((t_hp + hp[i], t_joy + joy[i]))
    dp.extend(arr)
    arr.clear()

# dp 마지막 중에 가장 큰 값 가져오기
dp.sort(reverse=True, key=lambda x: x[1])

if len(dp) == 0:
    print(0)
else:
    print(dp[0][1])
