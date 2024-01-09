# 현재 위치 기준으로 8가지를 체크해보면 될듯

pos = input()
row = int(pos[1])
col = ord(pos[0]) - ord('a') + 1

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

cnt = 0
# 상하좌우
for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]
    # 범위가 1 <= val <= 8 아니면 ... 즉 범위에 벗어나면 continue
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        cnt += 1

print(cnt)
