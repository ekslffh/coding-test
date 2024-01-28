# # 내 답안
# # n이 1이 될 때까지 1을 빼거나 k로 나누는 연산의 최소 횟수
# # 최대한 많이 나누는 것이 kick
#
# # n, k 입력받기
# n, k = map(int, input().split())
#
# # 반복하면서 n이 K로 나누어 질때까지 1로 빼고 k로 나눠주는 연산 반복
# # 이 때 둘 연산 진행하다가 1이 되면 나가기
# cnt = 0
# while n >= k:
#     # k로 나누어 떨어질때까지 1빼주기
#     while n % k != 0:
#         n -= 1
#         cnt += 1
#     # n으로 나누기
#     n //= k
#     cnt += 1
#
# # 1이 안된 경우
# if n > 1:
#     # n이 k보다 작아진 경우에 남은 횟수 1빼는 연산으로 투입
#     cnt += n - 1
#
# # 결과출력
# print(cnt)

# 책 답안
# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
