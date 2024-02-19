# A배열의 최소값과 B배열의 최대값을 스왑한다. 단, A배열의 최소값이 더 큰 경우에는 반복문 나가기
n, k = map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort() # 배열 A는 오름차순 정렬 수행
b_arr.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    min_val = a_arr[i]
    max_val = b_arr[i]
    # A배열의 최소값이 더 큰 경우에는 반복문 나가기
    if min_val >= max_val:
        break
    else: # 그렇지 않다면 스왑하기
        a_arr[i], b_arr[i] = b_arr[i], a_arr[i]

print(sum(a_arr)) # 배열 A의 모든 원소의 합을 출력
