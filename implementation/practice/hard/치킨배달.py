# 도시의 치킨거리(각 집과 가장 가까운 치킨집과의 거리의 합)의 최솟값을 구하기 (완전탐색)

# 순열 조합 사용하기
from itertools import combinations

# 도시의 크기 (n), 남겨둘 치킨집의 개수(m) 입력받기
n, m = map(int, input().split())
# n * n 도시의 정보 입력받기 (0: 빈곳, 1: 집, 2: 치킨집)
city = []
for i in range(n):
    data = list(map(int, input().split()))
    city.append(data)
# 도시를 돌면서 집의 위치정보, 치킨집의 위치정보 (행, 열)형식으로 저장하기
homes = []
restaurants = []
# 도시의 모든 곳 돌아보기
for i in range(n):
    for j in range(n):
        # 집 위치 저장
        if city[i][j] == 1:
            homes.append((i, j))
        # 치킨집 위치 저장
        elif city[i][j] == 2:
            restaurants.append((i, j))
# 치킨집 위치정보들 중에서 m개씩 고르는 경우의 수 구하기 (combinations)
restaurants_combinations = combinations(restaurants, m)
# m개씩 고른 경우의 수를 반복하면서 탐색하기

# 가장 먼거리가 98이므로 우선 기존 누적 값을 절대 넘을 수 없는 값 99 * 50으로 잡는다.
answer = 99 * 50
for group in restaurants_combinations:
    # m개의 치킨집의 위치가 정해졌을 때 집 정보 기준으로 가장 가까이 있는 치킨집의 거리를 구해서 각각을 더해준다.
    d_sum = 0
    for home in homes:
        home_x, home_y = home
        # 특정 집에 대한 치킨거리 구해보기 : 초기화값을 99로 잡는다.
        min_d = 99
        for restaurant in group:
            res_x, res_y = restaurant
            d = abs(home_x - res_x) + abs(home_y - res_y)
            min_d = min(min_d, d)
        # 여기까지 왔다면 특저 집에 대한 치킨거리가 구해졌다. 이를 누적으로 더해보자
        d_sum += min_d
    # 여기까지 왔다면 현재 조합에 대한 도시의 치킨거리가 구해졌다. (d_sum) 이를 answer과 비교해서 최솟값을 넣어주자
    answer = min(answer, d_sum)

# 치킨 거리의 최솟값 출력하기.
print(answer)
