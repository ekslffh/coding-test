# 주사위 윷놀이
from copy import copy

# 시작은 0, 도착은 31
graph = [
    [1], [2], [3], [4], [5],
    [6, 21], [7], [8], [9], [10],
    [11, 25], [12], [13], [14], [15],
    [16, 27], [17], [18], [19], [20],
    [32], [22], [23], [24], [30], [26], [24],
    [28], [29], [24], [31], [20], [32]
]

# 0 ~ 31번호 위치에 대한 점수
score = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 25,
    22, 24, 28, 27, 26, 30, 35, 0
]

dice = list(map(int, input().split()))
answer = 0

# 깊이, 합산점수, 현재 말의 위치 [?, ?, ?, ?]
def backtracking(depth, result, mal):
    global answer
    if depth == 10:
        answer = max(answer, result)
        return

    # 4개의 말을 각각 보내보는 로직 구현
    for i in range(4):
        temp_mal = copy(mal)
        x = temp_mal[i]

        # if x == 32:
        #     continue

        # 2갈래 길인경우(10, 20, 30), 파란색길로 보내
        if len(graph[x]) == 2:
            x = graph[x][1]
        else: # 아니면, 빨간색 길로
            x = graph[x][0]

        # 주사위 값만큼 이동해보기 (앞서 한칸 이동했으므로, 한칸 덜 이동하기)
        for _ in range(dice[depth] - 1):
            x = graph[x][0]

        if x == 32 or (x < 32 and x not in temp_mal):
            # 다음 상황으로 재귀 보내기
            temp_mal[i] = x
            backtracking(depth + 1, result + score[x], temp_mal)

backtracking(0, 0, [0, 0, 0, 0])
print(answer)
