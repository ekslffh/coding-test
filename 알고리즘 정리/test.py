import sys

data = input()
idx = 0
result = ''
while idx < len(data):
    cur_idx = idx
    cur_val = data[cur_idx]
    cnt = 0
    while idx < len(data) and cur_val == data[idx]:
        idx += 1
        cnt += 1
    if cur_val == '.':
        result += '.' * cnt
    else:
        if cnt % 2 == 1:
            print(-1)
            sys.exit()
        else:
            a_num = cnt // 4
            b_num = (cnt % 4) // 2
            result += 'AAAA' * a_num + 'BB' * b_num

print(result)
