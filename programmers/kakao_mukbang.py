# 성공...
def solution(food_times, k):
    answer = 0
    N = len(food_times)
    food_times = [[0,0]] + [[food_times[i], i + 1]for i in range(N)]
    food_times.sort()
    N += 1
    for i in range(1, N):
        if k > (food_times[i][0] -food_times[i - 1][0]) * (N - i):
            k -= (food_times[i][0] -food_times[i - 1][0]) * (N - i)
        elif k == (food_times[i][0] - food_times[i - 1][0]) * (N - i):
            for j in range(i + 1, N):
                if food_times[i][0] != food_times[j][0]:
                    food_times = food_times[j:]
                    food_times.sort(key=lambda x:x[1])
                    return food_times[0][1]
        else:
            food_times = food_times[i:]
            food_times.sort(key=lambda x:x[1])
            return food_times[(k % (N - i))][1]
    return -1
'''
정확성: 17.4
효율성: 7.1
합계: 24.6 / 100.0
'''
def solution(food_times, k):
    answer = 0
    N = len(food_times)
    cnt = N
    while k:
        a = k // cnt
        if a > 0:
            for i in range(N):
                if food_times[i] > a:
                    food_times[i] -= a
                    k -= a
                else:
                    k -= food_times[i]
                    food_times[i] = 0
                    cnt -= 1
        else:
            break
    while k:
        if food_times[answer]:
            food_times[answer] -= 1
            k -= 1
        answer += 1
        answer %= N
    return answer + 1