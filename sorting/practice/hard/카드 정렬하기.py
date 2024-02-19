# idea : 오름차순 정렬하여서 가장 작은 묶음부터 비교해보자

# 묶음 개수 N 입력받기
n = int(input())

# 카드묶음 개수 정보들 입력받기
cards = []
for _ in range(n):
    cards.append(int(input()))

# 정답을 저장할 변수
answer = 0
# 처음에 한번 정렬시키기
cards.sort()
# 반복을 시키되, 묶음이 한개가 될때까지
while len(cards) > 1:
    # 오름차순 정렬하여서 첫번째로 작은 카드와 두번째로 작은 카드를 합치기
    # 사간초과가 난다면? : 이미 정렬되어 있는 데이터에 하나의 데이터만 넣으면 되므로 괜히 sort() 사용하지말고, 삽입정렬을 수행해보자!
    first = cards[0]
    second = cards[1]
    answer += first + second
    # 합친 이후에 첫번째 두번째 카드는 제외하고, 합친 카드를 넣어주기
    cards = cards[2:]
    cards.append(first + second)
    # 만약 값이 하나라면 반복문 나가기
    if len(cards) == 1:
        break
    # 맨뒤에 합친 결과를 넣었고 이 데이터만 삽입정렬을 통해서 정렬시켜보자
    for i in range(len(cards) - 1, 0, -1):
        # 만약에 현재 값이 이전 값보다 작다면 둘이 스왑하기
        if cards[i] < cards[i - 1]:
            cards[i], cards[i - 1] = cards[i - 1], cards[i]
        else: # 그게 아니라면 나머지는 다 정렬되어 있으므로 해당 위치에서 break하면 된다.
            break

# 정답 출력하기
print(answer)
