# dp 테이블 생성
d = [0] * 30001

# 정수 x 입력받기
x = int(input())

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 1을 뺐을 때의 연산 횟수 먼저 저장
    d[i] = d[i - 1] + 1
    # 2,3,5 차례대로 나누어떨어진다면, 연산해보고 최솟값으로 갱신해주기
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
