import heapq

# N 입력받기
n = int(input())

# 카드묶음정보 입력받기
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

# 정답변수
answer = 0
while len(cards) > 1:
    # 최소값 a, b 추출하고 합치는 과정 수행
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a + b
    heapq.heappush(cards, a + b)

# 정답 출력하기
print(answer)
