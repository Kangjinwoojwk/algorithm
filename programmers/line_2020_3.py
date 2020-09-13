def solution(n):
    answer = [len(str(n)), n]
    def sol(n, d):
        if n < 10:
            if d < answer[0]:
                answer[0] = d
                answer[1] = n
            return
        for i in range(1, len(str(n))):
            if str(n)[-i] != '0':
                sol((n % (10 ** i)) + (n // (10 ** i)), d + 1)
    sol(n, 0)

    return answer