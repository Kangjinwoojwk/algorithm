# 정답
def solution(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b % 1000000007


# 효율성 테스트 2개 미통과
def solution(n):
    li = [0] * (n + 1)
    li[1] = 1
    li[2] = 2
    chk = 3
    while li[n] == 0:
        li[chk] = li[chk - 1] + li[chk - 2]
        chk += 1
    return li[n] % 1000000007