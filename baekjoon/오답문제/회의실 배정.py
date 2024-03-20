# 회의실 배정
n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
# 회의 종료 시간 기준 오름차순 정렬
data.sort(key=lambda x: (x[1], x[0]))

answer = [data[0]]

i = 1
cur = data[0]
while i < n:
    # 다음 회의 시작 시간 >= 현재 회의 종료 시간
    if data[i][0] >= cur[1]:
        answer.append(data[i])
        cur = data[i]
    i += 1

print(len(answer))
