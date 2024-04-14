def solution(n):
    answer = []
    # 삼각형 정보 배열 생성
    triangle = [[0] * x for x in range(1, n + 1)]
    # 왼쪽아래, 오른쪽, 왼쪽위
    steps = [(1, 0), (0, 1), (-1, -1)]
    # steps 순서대로 이동해보기
    x, y = 0, 0
    triangle[x][y] = 1
    while True:
        is_move = False
        for dx, dy in steps:
            nx = x + dx
            ny = y + dy
            # 범위 검사 and 방문 검사
            if nx < 0 or nx > n or ny < 0 or ny > nx or triangle[nx][ny] != 0:
                continue
            else: # 이동이 가능하고, 방문하지 않은 곳이라면, 이동해서 현재 걸음수 저장, 이동
                triangle[nx][ny] = triangle[x][y] + 1
                x, y = nx, ny
                is_move = True
                break
        # 이동하지 못했다는 것은, 마지막에 도달했다는 의미
        if not is_move:
            break
    # 순서대로 값에 넣어주기
    for x in range(n):
        for y in range(x + 1):
            answer.append(triangle[x][y])
    return answer

print(solution(4))
