# 분산처리

answer = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr = []
    result = 1
    for _ in range(4):
        result *= a
        arr.append(result % 10)
    answer.append(arr[b % 4 - 1])

for x in answer:
    if x == 0:
        print(10)
    else:
        print(x)
