n = int(input())

answer = [0] * 10

for x in range(1, n + 1):
    str_x = str(x)
    for i in str_x:
        answer[int(i)] += 1

for x in answer:
    print(x, end=' ')
