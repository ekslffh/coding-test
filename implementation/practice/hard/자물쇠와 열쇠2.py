import copy

def rotation(key):
    # 시계방향으로 90도 회전시키고 리턴
    new_key = copy.deepcopy(key)
    for row in range(len(key)):
        for col in range(len(key)):
            # 행 : 기존의 열, 열 : 자물쇠길이 - 1 - 기존의 행
            new_key[col][len(key) - 1 - row] = key[row][col]
    return new_key

def solution(key, lock):
    # 3N * 3N 크기의 확장맵을 만들고 가운데에 자물쇠를 위치해놓는다.
    n = len(lock)
    m = len(key)
    expand_map = [[0] * (3 * n) for _ in range(3 * n)]

    # 자물쇠 정보 넣어주기
    for x in range(n):
        for y in range(n):
            # 돌기라면 가운데쪽에 정보 넣어주기
            if lock[x][y] == 1:
                expand_map[x + n][y + n] = 1

    # 키를 90도씩 회전해야한다. (4가지)
    for _ in range(4):
        key = rotation(key)
        # 확장맵을 돌면서 키를 위치해두면서 두가지를 검사해야 한다.
        # 확장맵에 키를 넣을 때 시작지점은 0부터 확장맵길이 - 키의 길이
        for x in range(3 * n - m + 1):
            for y in range(3 * n - m + 1):
                # x, y부터 시작지점임
                em = copy.deepcopy(expand_map)
                for i in range(m):
                    for j in range(m):
                        em[x + i][y + j] += key[i][j]

                # 돌기가 만나지 않는지 확인
                if max(max(em, key=lambda x: max(x))) == 2:
                    continue

                # 가운데 부분이 다 채워졌는지 확인
                center = [row[n:2*n] for row in em[n:2*n]]
                if sum(sum(center, [])) == n * n:
                    return True

    # 모든 경우에 대해 실패하면 False 리턴
    return False
