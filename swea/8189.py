# 파이썬이 지원안된다 나중에 해보자 아니 C++로 해볼가?
for tc in range(1, int(input()) +1):
    N, A, B = map(int, input().split())
    t = list(map(int, input().split()))
    ans = [0] * N
    letter = list()
    for i in range(1, 2001):
        if t[0] == i:
            letter.append(t.pop(0))
            if len(letter) == A:
