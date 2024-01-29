# 0 ~ 9로만 이루어진 문자열 S에 대하여 사이 사이에 'X' or '+'를 넣어서 최대값을 출력하기
# 0이거나 1인경우, 더해주고 나머지는 곱하는 게 이득이다.

# 문자열 S 입력받기 (list형태로 받기)
data = list(map(int, input()))
# 하나씩 돌면서 result나 현재 수가 0,1이면 더하고, 이외에는 곱해주기
result = 0
for d in data:
    if result <= 1 or d <= 1:
        result += d
    else:
        result *= d

# 정답 출력
print(result)
