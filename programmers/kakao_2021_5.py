# 시간 복잡도 개선, 여전히 시간초과 존재
def solution(play_time, adv_time, logs):
    def time_trans(t):
        t = list(map(int, t.split(':')))
        return t[0] * 60 * 60 + t[1] * 60 + t[2]
    answer = 0
    max_time = 0
    play_time = time_trans(play_time)
    adv_time = time_trans(adv_time)
    logs = [[time_trans(i.split('-')[0]), time_trans(i.split('-')[1])] for i in logs]
    cnt = [0] * (((99 * 60) + 59) * 60 + 60)
    for i in logs:
        for j in range(i[0], i[1]):
            cnt[j] += 1
    max_time = sum(cnt[0:adv_time + 1])
    for i in logs:
        t = sum(cnt[i[0]:i[0] + adv_time])
        if t > max_time:
            max_time = t
            answer = i[0]
        elif t == max_time and answer > i[0]:
            answer = i[0]
    answer = [answer // 3600, (answer % 3600) // 60, answer % 60]
    answer = ':'.join(['0' + i if len(i) == 1 else i for i in map(str, answer)])
    return answer




# 시간 초과, 실패도 있다! 뭐지...?
def solution(play_time, adv_time, logs):
    def time_trans(t):
        t = list(map(int, t.split(':')))
        return t[0] * 60 * 60 + t[1] * 60 + t[2]
    def chk(start, end):
        t = 0
        for i in logs:
            if end < i[0] or start > i[1]:
                continue
            t += min(end, i[1], play_time) - max(start, i[0])
        return t
    answer = 0
    max_time = 0
    play_time = time_trans(play_time)
    adv_time = time_trans(adv_time)
    logs = [[time_trans(i.split('-')[0]), time_trans(i.split('-')[1])] for i in logs]
    answer = play_time - adv_time
    max_time = chk(answer, play_time)
    for i in logs:
        t = chk(i[0], i[0] + adv_time)
        if t > max_time:
            max_time = t
            answer = i[0]
        elif t == max_time and answer > i[0]:
            answer = i[0]
    answer = [answer // 3600, (answer % 3600) // 60, answer % 60]
    answer = ':'.join(['0' + i if len(i) == 1 else i for i in map(str, answer)])
    return answer