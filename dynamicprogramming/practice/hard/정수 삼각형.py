# 문제 : 삼각형의 크기 N과 정수 삼각형의 정보가 주어졌을 때, 선택된 합의 수가 최대가 되는 경로 선택하기
# 제한사항 : 대각선 왼쪽, 오른쪽으로만 이동 가능하다.

# 아이디어 : 맨 위에서부터 아래로 이동하면서 모든 곳에 값 저장하면서 이동해보기

# 삼각형 정보 입력받기
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 좌상, 우상 방향 저장 (x,y)
steps = [(-1, -1), (-1, 0)]

# 맨 위층부터 1 -> 2 -> 3 -> ... -> n - 1 -> n 개의 층정보가 들어가 있다.
# DP 테이블 생성
d = [[] for _ in range(n)]
# 0층은 0번 정보 들어가도록 한다.
d[0].append(data[0][0])

# 1 ~ n 까지 반복하기 i
for floor in range(2, n + 1):
    # 0 ~ i번 까지 반복하면서 위층 좌우 확인해서 최대값과 합치기
    # 제한사항 (n층일때) : 0 <= 좌상, 우상 < n - 1 이어야지 범위를 벗어나지 않음.
    for x in range(floor):
        # floor 층의 x번째 원소 : data[floor -  1][x] => data[x][y]
        dx = floor - 1
        dy = x

        # 좌상 우상 이동해보기
        result = 0
        for step in steps:
            nx = dx + step[0]
            ny = dy + step[1]
            # 범위를 벗어나는지 확인하기 0 <= 좌상, 우상 < floor - 1 이어야지 범위를 벗어나지 않음.
            if ny < 0 or ny >= floor - 1:
                continue
            # 범위를 벗아나지 않으면 둘중에 큰 값을 골라야 한다.
            result = max(result, d[nx][ny])

        # 좌상 우상 중에 큰 값을 골라서 현재 값과 더해주기
        d[floor - 1].append(result + data[dx][dy])

# 1층에 대해서 최대값 출력하기
print(max(d[n - 1]))
