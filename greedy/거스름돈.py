# 500, 100, 50, 10원일 때 거스름돈으로 주는 동전의 개수 최소화
# 가장 액수가 큰 500원부터 최대한 많이 사용하기

coins = [500, 100, 50, 10]
n = int(input("거슬러 줘야 할 돈은? "))
result = 0
for coin in coins:
    result += n // coin
    n %= coin

print(result)
