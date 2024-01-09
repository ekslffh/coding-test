# 배열의 크기, 숫자가 더해지는 횟수, 최대 연속으로 더해질 수 있는 횟수 입력받기
n, m, k = map(int, input().split())
# 숫자 리스트 입력받기 (n개)
arr = list(map(int, input().split()))

# 내림차순 정렬
arr.sort(reverse=True)

# 하나의 세트는 가장 큰 수 k개 + 두번째로 큰 수 1개
num_set = arr[0] * k + arr[1]

# 결과는 세트개수랑 나머지는 가장 큰수로 더해주면 된다.
result = num_set * (m // (k + 1)) + arr[0] * (m % (k + 1))

print(result)
