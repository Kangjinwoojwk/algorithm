# 시간 폭탄, 제거 1초, 폭탄 터지는 시각 주어짐, 터지면 끝
# 몇개나 제거 가능한가?
def solution(bombs):
    bombs.sort()
    n = len(bombs)
    answer = 0
    time = 1
    i = 0
    while i < n:
        if bombs[i] >= time:
            answer += 1
            time += 1
        else:
            break
        i += 1
    return answer