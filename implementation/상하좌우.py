n = int(input())
move_info = list(input().split())

cur_x = 1
cur_y = 1
for move in move_info:
    if move == 'L' and cur_y > 1:
        cur_y -= 1
    elif move == 'R' and cur_y < n:
        cur_y += 1
    elif move == 'U' and cur_x > 1:
        cur_x -= 1
    elif move == 'D' and cur_x < n:
        cur_x += 1

print(cur_x, cur_y)
