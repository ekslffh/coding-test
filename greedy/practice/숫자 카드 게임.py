# 선택된 행중 가장 낮은 숫자를 뽑아서 결과적으로 가장 큰 숫자 뽑기
# 각 행 입력받을 때마다 최소값 구해서 그 중 최대값 비교하기

# 행n과 열 (m) 입력받기
n, m = map(int, input().split())

# n번 반복하면서 열의 정보 입력받기
result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    # 특정 행의 가장 작은 값 구하기
    min_val = min(data)
    # 작은 값 중 가장 큰 값으로 정답저장
    result = max(result, min_val)

# 결과 출력
print(result)
