# Fly me to the Alpha Centauri
t = int(input())

answer = []
for _ in range(t):
    x, y = map(int, input().split())
    n = y - x
    arr = [[] for _ in range(n + 1)]
    # (이동한 거리, 이동한 횟수)
    arr[0].append((0, 0))

    steps = [-1, 0, 1]

    # dp: bottom-up
    for i in range(n):
        for dist, cnt in arr[i]:
            # 이동 가능 거리 [k - 1, k, k + 1]
            for step in steps:
                next_step = dist + step
                # 다음 위치 = 현재 인덱스 + 이동 거리
                next_pos = i + next_step
                if i < next_pos <= n:
                    arr[next_pos].append((next_step, cnt + 1))

    result = [x[1] for x in arr[n] if x[0] == 1]
    answer.append(min(result))

for x in answer:
    print(x)
