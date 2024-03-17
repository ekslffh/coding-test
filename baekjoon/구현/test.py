def solution(routes):
    answer = 0

    # 두 범위가 교집합이 있는지 확인하는 함수
    def check(camera, car):
        if car[1] < camera[0] or car[0] > camera[1]:
            return False
        return True

    # 카메라의 범위를 차의 정보에 의해 조정해주는 함수
    def adjust(camera, car):
        # 진입 지점 조정
        camera[0] = max(camera[0], car[0])
        # 진출 지점 조정
        camera[1] = min(camera[1], car[1])

    camera = []
    routes.sort(key=lambda x: x[1])
    # 차량 이동경로에 따라서 카메라 범위를 생성 및 조정해보기
    for route in routes:
        is_possible = False
        for i in range(len(camera)):
            # 일치하면 카메라 범위 조정해주고 반복문 나가기
            if check(camera[i], route):
                adjust(camera[i], route)
                is_possible = True
                break
            # 일치하지 않으면 그냥 다음 반복문 실행 (다음 카메라 검사)
        # 여기까지 왔는데, 가능한 단속 카메라가 없으면 그 범위로 새로 달아보기
        if not is_possible:
            camera.append(route)
    answer = len(camera)
    return answer


routes = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]
print('정렬전', routes)
routes.sort(key=lambda x: x[1])
print('정렬후', routes)
print(solution(routes))
