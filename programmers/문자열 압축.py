def solution(s):
    answer = len(s)
    N = answer
    for i in  range(1, N // 2 + 1):
        cnt = N
        chk = 1
        for j in range(0, N, i):
            if s[j:j + i] == s[j + i: j + i + i]:
                cnt -=i
                chk += 1
            else:
                if chk > 1:
                    cnt += len(str(chk))
                chk = 1
        if cnt < answer:
            answer = cnt
    return answer