def solution(users, emoticons):
    # 각 이모티콘의 할인율을 설정하고, (가입자 수, 총 판매액) 형태로 저장할 배열
    answer = []

    # 할인율은 10, 20, 30, 40 중에 하나이다.
    sales = [10, 20, 30, 40]

    # 모든 이모티콘의 할인율이 설정이 되면, 가입자 수, 총 판매액 계산하는 함수
    def calc(arr):
        # 가입자 수
        subscriber_cnt = 0
        # 총 판매액
        sales_amount = 0
        # 모든 유저 돌면서, 판매액 and 가입여부 계산하기
        for user in users:
            # 현재 유저에 대한 판매액
            user_amount = 0
            # user_set_sale : 유저가 설정한 할인율 (이 이상이 되면 전부 구매)
            # user_set_amount : 유저가 설정한 최대 구매금액 (이 이상이 되면 임티 플러스 구매)
            user_set_sale, user_set_amount = user
            # 현재 설정된 할인율 돌면서 계산하기
            for i in range(len(arr)):
                # 할인율이 유저가 원하는 퍼센트보다 크면 산다.
                if arr[i] >= user_set_sale:
                    # 해당하는 이모티콘에 할인율 적용해서 더해주기
                    discount_emoticon = int(emoticons[i] * ((100 - arr[i]) * 0.01))
                    user_amount += discount_emoticon
                    # 총합이 유저가 설정한 맥시멈의 이상이라면, 무효하고 임티 플러스 가입
                    if user_amount >= user_set_amount:
                        user_amount = 0
                        subscriber_cnt += 1
                        break
            # 총합에 유저가 산 금액 더해주기
            sales_amount += user_amount
        # 여기서 (임티 가입자 수, 총 판매액) 리턴하기
        return (subscriber_cnt, sales_amount)

    # 현재 뎁스를 고려하여 할인율 적용해주며, 재귀하기
    def dfs(arr, depth):
        # 마지막 이모티콘까지 할인율 세팅된 경우
        if depth > len(emoticons):
            # 가입자 수, 총 판매액 계산해서 answer에 추가
            cnt, amt = calc(arr)
            answer.append((cnt, amt))
        else: # 아직 다 설정이 안된 경우
            for sale in sales:
                arr.append(sale)
                dfs(arr, depth + 1)
                arr.pop()

    # 빈배열로 1번부터 시작
    dfs([], 1)
    # answer 정렬 기준
    # 1. 가입자수 내림차순, 2. 금액 내림차순
    answer.sort(key=lambda x: (-x[0], -x[1]))

    # 정렬된 첫번째 원소 리턴하기
    return answer[0]
