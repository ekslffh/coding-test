# N개의 동전이 주어졌을 때, 만들 수 없는 최소 금액을 출력하기

# 검사해야 할 target금액은 1부터 가는데 만약에 현재 동전이 target보다 크면 불가능하다.

# 동전의 개수 N 입력받기
n = int(input())
# N개의 동전 입력받기 (중복 가능)
coins = list(map(int, input().split()))
# 오름차순 정렬
coins.sort()

# target은 1부터
target = 1
# 동전들 돌면서 만들 수 없는 금액 찾기
for coin in coins:
    # 만약에 현재 동전이 target보다 크면 불가능하다.
    if target < coin:
        break
    else: # target 만들기 불가능
        target += coin

# 정답출력 : 만약 끝까지 가더라도 다 더한 금액에서 1을 더한 상태가 정답이므로 그대로 출력한다.
print(target)
