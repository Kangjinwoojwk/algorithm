def solution(N):
    answer = [0, 0]
    for i in range(9, 1, -1):
        n = N
        multi = 1
        while n:
            x = n % i
            if x:
                multi *= x
                n //= i
        if multi > answer[1]:
            answer[0] = i
            answer[1] = multi
    return answer