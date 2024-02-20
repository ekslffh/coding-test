# n개의 부품들을 정렬하여 이진탐색을 수행하여 m개의 부품을 확인해보기 : 있으면 yes, 없으면 no 출력하기

# 부품의 개수 n 입력받기
n = int(input())
# n개의 부품 정보 입력받기
data = list(map(int, input().split()))
# 부품들 오름차순 정렬해놓기
data.sort()
# 찾는 부품의 개수 m 입력받기
m = int(input())
# 찾는 m개의 부품 정보 입력받기
reqs = list(map(int, input().split()))
# 이진 탐색 함수 정의 (재귀)
def binary_search_recursion(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid - 1)
    else:
        return binary_search_recursion(array, target, mid + 1, end)

# 이진 탐색 함수 정의 (반복)
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return True
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return False

# m개의 부품에 대하여 이진 탐색 수행하여 정답 출력하기
for req in reqs:
    # 특정 부품이 있는지 이진탐색 수행하기
    if binary_search_recursion(data, req, 0, len(data) - 1):
        # 존재하면 yes 출력
        print('yes', end=' ')
    else: # 존재하지 않으면 no 출력
        print('no', end=' ')

# 계수정렬이나 set자료형을 이용하여 구현할 수 도 있다.
