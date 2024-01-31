# https://school.programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    # 정답 리스트
    answer = []

    # 현재 건축 상태가 가능한 상태인지 검사하는 함수 (가능하면 True 리턴)
    def check(infos):
        # 현재 지어져 있는 건축상태 돌아보기
        for info in infos:
            # x, y, 건축물 종류
            x, y, a = info
            # 기둥이라면 1. 바닥이거나 2. 양쪽에 보가 하나라도 있거나 3. 양쪽이 모두 '보'여야 유지가능
            if a == 0:
                # 전부 실패하면 False 리턴하기
                if not (y == 0 or [x - 1, y, 1] in infos or [x, y, 1] in infos or [x, y - 1, 0] in infos):
                    return False
            # 보라면 1. 밑에 한쪽이라도 기둥이거나 2. 양쪽이 모두 '보'여야 유지가능
            elif a == 1:
                # 전부 실패하면 False 리턴하기
                if not ([x, y - 1, 0] in infos or [x + 1, y - 1, 0] in infos or ([x - 1, y, 1] in infos and [x + 1, y, 1] in infos)):
                    return False
        # 모든 검사를 통과한 경우 True 리턴
        return True

    # 건축순서 순서대로 수행
    for frame in build_frame:
        # x, y, 건축물종류, 설치 or 삭제 여부
        x, y, a, b = frame
        # 삭제 수행
        if b == 0:
            # 삭제해보기
            answer.remove([x, y, a])
            # 검사실패하면 다시 넣어주기
            if not (check(answer)):
                answer.append([x, y, a])
        # 설치 수행
        elif b == 1:
            # 설치해보기
            answer.append([x, y, a])
            # 검사실패하면 삭제하기
            if not (check(answer)):
                answer.remove([x, y, a])

    # 오름차순 정렬
    answer.sort()

    # 결과 리턴
    return answer
