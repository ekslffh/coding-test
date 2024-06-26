# 브랜드 중, 최소 패키지 값과 최소 낱개 값을 구한 후 3가지 경우 비교하기.
# 1. 패키지, 2. 패키지 + 낱개, 3. 낱개로

# 데이터 입력받으면서, 최소값 구하기.
n, m = map(int, input().split())
min_package = 1000
min_each = 1000
for _ in range(m):
    package_val, each_val = map(int, input().split())
    min_package = min(min_package, package_val)
    min_each = min(min_each, each_val)

answer = []
# 3가지 경우 구해보기.
p_val, e_val = n // 6, n % 6
# 1. 패키지로만 사기
if e_val > 0:
    answer.append((p_val + 1) * min_package)
else:
    answer.append(p_val * min_package)
# 2. 패키지 + 낱개
result = min_package * p_val + min_each * e_val
answer.append(result)
# 3. 낱개로만 사기
answer.append(n * min_each)

print(min(answer))
