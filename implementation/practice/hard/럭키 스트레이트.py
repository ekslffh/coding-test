# 점수를 반으로 나누어서 왼쪽의 합과 오른쪽의 합이 같아야지 스트레이트 가능

# # 점수 입력받고
# n = input()
# # 반으로 나누어서 left, right로 구분하기
# # 중간 포인트 찾기
# mid = len(n) // 2
# left = n[:mid]
# right = n[mid:]
# # 각각의 합을 구해서 같은지 비교
# left_sum = 0
# right_sum = 0
# for i in range(mid):
#     left_sum += int(left[i])
#     right_sum += int(right[i])
#
# # 같으면 LUCKY else READY 출력
# if left_sum == right_sum:
#     print("LUCKY")
# else:
#     print("READY")

# 풀이 2.
n = input()
mid = len(n) // 2
l_sum = sum(list(map(int, n[:mid])))
r_sum = sum(list(map(int, n[mid:])))
if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")
