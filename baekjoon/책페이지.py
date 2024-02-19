n = int(input())

answer = [0] * 10

d = []

# 숫자를 각각 자르는 방법
num = 330

for num in range(1, n + 1):
    num_to_str = str(num)
    for n in num_to_str:
        answer[int(n)] += 1

for a in answer:
    print(a, end=' ')
