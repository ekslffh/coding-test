# N번째 못생긴 수 구하기 (못생긴 수란, 소인수로 2,3,5만을 가지는 수이다.)
import time

n = int(input())
dp = {}
answer = 1
cnt = 0
start = time.time()
while True:
    dp[answer] = []
    num = answer
    while num != 1:
        if num != answer and num in dp:
            print(f"answer은 {answer} 이고, num은 {num}")
            dp[answer].extend(dp[num])
            break
        else:
            for i in range(2, answer + 1):
                if num % i == 0:
                    num //= i
                    dp[answer].append(i)
                    break
    is_ugly = True
    extra_values = set(dp[answer]) - {2, 3, 5}
    if extra_values:
        is_ugly = False
    if is_ugly:
        cnt += 1
        if cnt == n:
            break
    answer += 1

end = time.time()
print(answer)
print("시간 : ", end - start)
