# 각 집들과 안테나 사이의 거리의 합이 최소가 되는 위치를 출력하기. 단, 집이 위치한 곳에만 설치가 가능하다.

# 집의 개수 입력받기
n = int(input())

# 집의 위치 입력받기
homes = list(map(int, input().split()))

# 오름차순으로 정렬하기
homes.sort()

# 만약에 홀수라면 바로 중간값 출력하고, 짝수라면 가운데 두개 비교해보기
if len(homes) % 2 != 0:
    print(homes[len(homes) // 2])
else:
    mid_idx1 = len(homes) // 2
    mid_idx2 = mid_idx1 - 1
    sum1 = 0
    sum2 = 0
    for x in homes:
        sum1 += abs(x - homes[mid_idx1])
        sum2 += abs(x - homes[mid_idx2])
    if sum1 < sum2:
        print(homes[mid_idx1])
    else:
        print(homes[mid_idx2])
