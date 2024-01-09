# 각 행마다 가장 작은 수를 고르는데 결과적으로 그중에서 가장 큰 수가 뽑히도록 하자

# 행, 열 입력받기
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 값 찾기
    min_value = min(data)
    # 작은 값 중에 가장 큰 값 찾기
    result = max(result, min_value)

print(result)
