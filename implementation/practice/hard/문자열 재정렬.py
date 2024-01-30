# 알파벳 대문자와 숫자로만 구성된 문자열을 알파벳을 오름차순 정렬하고 맨뒤에 숫자들의 합으로 출력하기

# 문자열 입력받기
s = input()

# 반복문 돌면서 문자열인지 숫자인지 구분하기
# 1. 문자열이면 문자열 리스트에 담아주고 2. 숫자면 더해주기
s_arr = []
s_sum = 0
for x in s:
    # 숫자라면 sum에 더해주기
    if x.isdigit():
        s_sum += int(x)
    # 문자면 배열에 추가
    elif x.isalpha():
        s_arr.append(x)

# 알파벳 오름차순 정렬
s_arr.sort()
# 숫자합 추가
s_arr.append(s_sum)

for x in s_arr:
    print(x, end='')
