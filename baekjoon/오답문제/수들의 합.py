# 서로 다른 N개의 자연수의 합이 S라고 할때, 자연수의 N의 최대값은?
# N이 최대가 되기 위해서는 가장 작은 자연수인 1부터 차례대로 더해줘야 한다.

# 자연수의 합 입력받기
s = int(input())

# s를 안넘을 때까지 1부터 차례대로 더해주기
hap = 0
num = 0
while (hap + num + 1) < s:
    num += 1
    hap += num

# (s - hap) 이  num 보다 작거나 같으면 숫자가 중복되므로 불가
while (s - hap) <= num:
    hap -= num
    num -= 1

# 1을 더해준 값이 정답이 된다.
answer = num + 1
# 만약, 딱 떨이지게 s를 구했다면 1을 빼준다.
if hap == s:
    answer -= 1

# 정답은 num에 1을 더해준 값이다.
print(answer)
