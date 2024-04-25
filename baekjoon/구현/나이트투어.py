# 6 x 6 체스판에 모든 경로 가보면서, 검사해보기

def get_pos(pos):
    data = list(pos)
    x = ord(data[0]) - ord('A') + 1
    y = int(data[1])
    return x, y

# 이동경로 저장할 배열
arr = []

# 나이트가 갈 수 있는 8가지 경로
steps = [(-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1), (-2, -1)]

# 유효한지 상태 저장변수
is_valid = True
# 36번 이동경로 입력받기
for _ in range(36):
    # 이동할 위치 입력받기
    ax, ay = get_pos(input())
    # 1. 중복검사 시행
    if (ax, ay) in arr:
        is_valid = False
        break
    else:
        # 2. 가능 이동경로인지 검사
        # 만약 첫 이동이라면 바로 가능
        if not arr:
            arr.append((ax, ay))
        else:
            x, y = arr[-1]
            # 해당 경로가 포함되는지 확인
            is_exists = False
            for dx, dy in steps:
                # 이동해보기
                nx = x + dx
                ny = y + dy
                if 1 <= nx <= 6 and 1 <= ny <= 6 and (nx, ny) == (ax, ay):
                    arr.append((nx, ny))
                    is_exists = True
                    break
            # 포함되지 않았다면, is_valid = False
            if not is_exists:
                is_valid = False
                break

if is_valid and arr[-1] != (1, 6):
    print("Valid")
else:
    print("Invalid")
