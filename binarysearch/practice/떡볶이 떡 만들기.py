# 이진 탐색을 이용하여 적정한 떡의 길이르 잴 수 있을 까?

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
data = list(map(int, input().split()))

# 우선 정답은 최대 길이 0으로 설정
answer = 0

def get_height(array, height):
    result = 0
    for x in array:
        # 절단기의 높이가 특정 떡의 길이보다 작아야지 떡이 잘린다.
        if height < x:
            result += x - height
    return result

# 높이의 최대값을 구하는 이진탐색 함수
def binary_search(array, target, start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        # 높이를 설정하여 잘린 떡의 길이 구하기
        result = get_height(array, mid)
        # 잘린 떡의 길이가 target 이상이면 정답후보로 올리고 절단기의 높이를 더 늘려보기
        if result >= target:
            answer = mid
            start = mid + 1
        # 잘린 떡의 길이가 target 미만이면 절단기의 높이를 줄여야 한다.
        else:
            end = mid - 1

# 이진탐색 수행
binary_search(data, m, 0, max(data) - 1)

# 정답 출력
print(answer)
