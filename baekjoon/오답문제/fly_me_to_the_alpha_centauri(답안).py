# Fly me to the Alpha Centauri

# 거리(y - x)에 따라 계산해보면 딱떨어지는 제곱근을 기준으로 소수점의 범위에 따라 값이 조금씩 달라지는 규칙을 발견할 수 있다.
import math

# t번 반복할게요.
t = int(input())

# 정답 넣어줄 배열 선언할게요.
answer = []
for _ in range(t): # t번 돌면서
    # 출발지, 도착지 입력받고 거리 계산하기
    x, y = map(int, input().split())
    dist = y - x
    # 제곱근 구하고 정수와 소수 구분하기
    square_root = math.sqrt(dist)
    integers = int(square_root)
    decimals = square_root - integers
    # 1, 2, 4와 같이 딱떨어질때 값 구하기
    result = integers * 2 - 1
    # 소수점이 0은 아니고 0.5보다 작은 경우 + 1
    if decimals != 0:
        if decimals < .5:
            result += 1
        else: # .5보다 큰경우에는 +2
            result += 2
    # 현재 반복문 정답 배열에 넣기
    answer.append(result)

# 전체 정답 결과 출력하기
for x in answer:
    print(x)
