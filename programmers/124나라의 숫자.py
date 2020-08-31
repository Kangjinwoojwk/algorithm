def solution(n):
    answer = ''
    while n:
        if n % 3 == 1:
            answer = '1' + answer
        elif n % 3 == 2:
            answer = '2' + answer
        else:
            n -= 1
            answer = '4' + answer
        n //= 3
    return answer