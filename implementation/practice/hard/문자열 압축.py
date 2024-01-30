# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # 시작최대길이는 s의 길이로 시작
    answer = len(s)

    # 문자열을 압축하여서 가장 짧은 것의 길이를 리턴하기
    # 자르는 단위는 1 ~ (문자열의 길이 // 2) (완전탐색문제)
    max_unit = len(s) // 2

    # 전체 단위에 대하여 검사해보기 (1 ~ 절반길이)
    for unit in range(1, max_unit + 1):
        # 압축된 문자열 초기화
        result = ''
        # 시작 기준 잡아주기
        prev = s[:unit]
        # 반복되는 횟수
        cnt = 1
        # 전체 문자열을 돌면서 검사하는데 뛰어넘는 기준을 unit으로 주면 unit만큼뛰면서 반복할듯
        for x in range(unit, len(s), unit):
            now = s[x:x + unit]
            # 같으면 카운트
            if now == prev:
                cnt += 1
            # 이전값과 현재값이 다를 때의 처리
            else:
                # 1. 만약 반복되는 카운트가 1보다 크다면 cnt를 붙여주고 prev값 붙여주고 cnt초기화
                if cnt > 1:
                    result += str(cnt) + prev
                    cnt = 1
                # 2. 만약 1이라면 그냥 붙여주기
                else:
                    result += prev
                # prev를 now걸로 교체해줘야 함.
                prev = now

        # 마지막 부분에서의 처리
        # 1. 끝까지 반복되다가 끝난 경우
        if cnt > 1:
            result += str(cnt) + prev
            cnt = 1
        # 2. 만약 1이라면 그냥 붙여주기
        else:
            result += prev

        answer = min(answer, len(result))
        # print(result)

    return answer

s = input()
answer = solution(s)
print(answer)
