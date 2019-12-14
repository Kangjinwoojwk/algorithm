def solution(n):
    answer = 0
    data = {int(i) for i in str(n) if i!='0'}
    for i in data:
        if n % i == 0:
            answer += 1
    return answer