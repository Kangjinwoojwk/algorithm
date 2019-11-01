# 투썸, 매일 1번 당첨, 가장 빠른 중복당첨자는?
def solution(arr):
    answer = 1<<30
    lucky = dict()
    for i in range(len(arr)):
        if arr[i] in lucky:
            if i - lucky[arr[i]] <  answer:
                answer = i - lucky[arr[i]]
        lucky[arr[i]] = i
    if answer == 1<<30:
        answer = -1
    return answer