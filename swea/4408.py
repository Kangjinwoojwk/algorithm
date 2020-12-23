for tc in range(1, int(input()) + 1):
    N = int(input())
    room = [0] * 200
    for _ in range(N):
        s, e = map(int, input().split())
        s = (s - 1) // 2
        e = (e - 1) // 2
        if s > e:
            s, e = e, s
        for i in range(s, e + 1):
            room[i] += 1
    print('#{} {}'.format(tc, max(room)))