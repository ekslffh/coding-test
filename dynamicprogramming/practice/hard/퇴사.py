# N + 1 일째 되는날 퇴사하기 전에 상담을 진행하며 최대 수익을 내기

# 데이터 입력받기
n = int(input())
data = []
for _ in range(n):
    # 시간(t), 금액(p)
    t, p = map(int, input().split())
    data.append((t, p))

# dp 테이블 선언하고 0으로 초기화 ( 1 ~ n )
d = [0] * (n + 1)

# 정답 넣어줄 변수 선언하고 0으로 초기화
answer = 0
# 1 ~ n 일차 까지 이동하기
for day in range(1, n + 1):
    t, p = data[day - 1]
    # day + t 가 n + 1을 넘어가면 상담 불가하다.
    if day + t > n + 1:
        continue
    # 현재 상담을 퇴직 전에 끝낼 수 있다면, answer의 값을 비교하여 갱신해보기 : 현재까지의 최대 비용
    cur_val = d[day] + p
    answer = max(answer, cur_val)
    # day + t 이후에 값들도 갱신해보기
    for i in range(day + t, n + 1):
        d[i] = max(d[i], cur_val)

# 정답 출력
print(answer)
