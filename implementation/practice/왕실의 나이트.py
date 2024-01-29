# # 내풀이
# # 나이트가 이동할 수 있는 위치가 몇개인지 구하기
# # 총 8곳으로 이동을 시도해 볼 수 있다.
#
# # 8가지 방향 정의하기 (상하좌우)
# dx = [-2, -2, 2, 2, -1, 1, -1, 1]
# dy = [-1, 1, -1, 1, -2, -2, 2, 2]
#
# pos = input()
#
# # x, y좌표 구하기 (zero base)
# x = int(pos[1]) - 1
# y = ord(pos[0]) - ord('a')
#
# result = 0
# # 8가지 방향으로 이동해보기
# for i in range(8):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     # 범위를 벗어나는지 확인
#     if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
#         continue
#     result += 1
#
# print(result)

# 해설 풀이
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
