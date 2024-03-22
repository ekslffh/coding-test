king, stone, n = input().split()
move_info = [input() for _ in range(int(n))]

move_dict = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

# 문자 -> 아스키코드
def encode(c):
    return ord(c) - ord('A')

# 아스키코드 -> 문자
def decode(c):
    return chr(c + ord('A'))

# 0,0 부터
kx, ky, sx, sy = encode(king[0]), int(king[1]) - 1, encode(stone[0]), int(stone[1]) - 1

# 이동해보기
for info in move_info:
    dx, dy = move_dict[info]
    nx = kx + dx
    ny = ky + dy
    # 돌이랑 만났을 때, 돌도 같은 방향으로 이동 시키기
    nsx, nsy = sx, sy
    if nx == sx and ny == sy:
        nsx += dx
        nsy += dy
    # 범위 검사
    if (0 <= nx < 8) and (0 <= ny < 8) and (0 <= nsx < 8) and (0 <= nsy < 8):
        kx, ky, sx, sy = nx, ny, nsx, nsy

# 이동한 후에 위치 구하기
kx = decode(kx)
sx = decode(sx)
ky += 1
sy += 1

# 정답 출력 (왕, 돌의 위치 순서대로)
print(kx + str(ky))
print(sx + str(sy))
