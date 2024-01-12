# 두 배열 A, B가 있을 때 원소를 최대 K번 교체하여 A의 원소의 합이 최대가 되도록 하기

# 원소의 개수, 교체횟수 입력받기
n, k = map(int, input().split())

# a,b 배열 원소 정보 입력받기
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

# a는 오름차순, b는 내림차순 정렬
a_arr.sort()
b_arr.sort(reverse=True)

for i in range(k):
    # A의 원소가 B의 원소보다 더 작을 경우
    if a_arr[i] < b_arr[i]:
        # 두 원소를 교체
        a_arr[i], b_arr[i] = b_arr[i], a_arr[i]
    else:   # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a_arr))
