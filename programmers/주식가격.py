# 정답 코드, 한번만 보려고 발악했는데 그럴 필요 없다 n^2가 낫다
def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
        else:
            answer[i] = j - i

    return answer



# 정확성 통과 효율성 전부 시간초과
def solution(prices):
    answer = []
    day_length = [0]*10001
    while prices:
        i = prices.pop()
        answer = [day_length[i]] + answer
        for j in range(i + 1):
            day_length[j] += 1
        for j in range(i + 1, 10001):
            day_length[j] = 1
    return answer