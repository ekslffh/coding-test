# 최대한 많이 나누기 : 나눌 수 있을 때 까지 빼고 바로 나누기

n, k = map(int, input().split())
cnt = 0

while n >= k:
    # k로 나누어 떨어지면 나누기
    if (n % k) == 0:
        n //= k
        cnt += 1
    # 안 나누어 지면 나누어 질 때까지 1로 빼기
    else:
        while (n % k) != 0:
            n -= 1
            cnt += 1

while n > 1:
    n -= 1
    cnt += 1

print(cnt)
