# c개의 공유기를 n개의 집에 설치하여, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 값 구하기

n, c = map(int, input().split())

data = []

for _ in range(n):
    data.append(int(input()))
data.sort()

# 최소거리는 1, 최대거리는 마지막 - 첫번째 원소값
start = 1
end = data[n - 1] - data[0]

answer = -1

# 시작, 끝 점을 가지고 중간값을 갱신하며 값 구해보기
while start <= end:
    # 현재 최대 값을 중간값으로 설정
    mid = (start + end) // 2
    # 첫번째 집에 공유기 설치
    prev = data[0]
    cnt = 1
    # 앞에서부터 공유기 설치해보기
    for i in range(1, n):
        # 두 거리가 mid값을 충족하면 안테나 설치하고 이전값 갱신
        if (data[i] - prev) >= mid:
            cnt += 1
            prev = data[i]
    # 설치된 공유기 개수가 c 이상이면 정답 갱신하고 거리를 늘려보기
    if cnt >= c:
        answer = mid
        start = mid + 1
    # 설치된 공유기 개수가 c 보다 작다면 거리를 줄여보기
    else:
        end = mid - 1
# 정답 출력
print(answer)
