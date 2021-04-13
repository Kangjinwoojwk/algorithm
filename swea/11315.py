T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
di = [1, 1, 1, 0, -1, -1, -1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
for test_case in range(1, T + 1):
    n = int(input())
    stage = [input() for _ in range(n)]
    answer = 'NO'
    for i in range(n):
        for j in range(n):
            if stage[i][j] == 'o':
                chk = [True] * 8
                for k in range(1, 5):
                    for l in range(8):
                        if i + (k * di[l]) < 0 or j + (k * dj[l]) < 0 or i + (k * di[l]) >= n or j + (k * dj[l]) >= n or stage[i + (k * di[l])][j + (k * dj[l])] == '.':
                            chk[l] = False
                    if True not in chk:
                        break
                else:
                    if True in chk:
                        answer = 'YES'
            if answer == 'YES':
                break
        if answer == 'YES':
            break
    print('#{} {}'.format(test_case, answer))