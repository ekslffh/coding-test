# https://www.acmicpc.net/problem/14248

# 깊이 우선 탐색을 이용하여 양방향으로 보내보기

n = int(input())
stones = list(map(int, input().split()))
start = int(input())

def dfs(x):
    if x in result:
        return
    result.append(x)
    stone_number = stones[x - 1]
    left_position = x - stone_number
    if left_position >= 1:
        dfs(left_position)
    right_position = x + stone_number
    if right_position <= n:
        dfs(right_position)

result = []
dfs(start)
print(len(result))
