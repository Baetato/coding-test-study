import sys
input = sys.stdin.readline

N, M, D = map(int, input().split()) # N, M, D 입력받기
board = [list(map(int, input().split())) for _ in range(N)] # N X M 사이즈의 2차원 배열 만들기


# 세번째 예제부터 이해가 안되기 시작..
    # - 궁수는 3명 한정이고 모두 동시에 공격하고, 각 턴에 한번만 공격할 수 있는데 어떻게 예제 3에서 제거할 수 있는 적의 최대 수가 5명이 되는거지
    # - 2명 추가 제거는 성에 도착해서 제거되는거지 궁수의 공격으로 인해 제거되는 것이 아니지 않나?