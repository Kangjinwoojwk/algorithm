'''
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    rotate_key = [[key[i][j] for j in range(M)] for i in range(M)]
    def check(key, lock, M, N):
        for i in range(-M + 1, N):
            for j in range(-M + 1, N):
                go = True
                for k in range(M):
                    for l in range(M):
                        if 0 <= k + i < N and 0 <= l + j < N:
                            if key[k][l] == lock[k + i][l + j]:
                                go = False
                                break
                    if not go:
                        break
                else:
                    for k in range(N):
                        for l in range(N):
                            if i <= k < i + M and j <= l < j + M:
                                continue
                            elif lock[k][l] == 0:
                                go = False
                                break
                        if not go:
                            break
                    else:
                        return True
        return False
    for i in range(4):
        answer = check(rotate_key, lock, M, N)
        rotate_key = [[rotate_key[M - 1 - j][i] for j in range(M)] for i in range(M)]
        if answer:
            break
    return answer