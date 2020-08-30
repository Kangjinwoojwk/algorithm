def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = [ (100 - progresses[i] + speeds[i] - 1 )//speeds[i] if (100 - progresses[i]) % speeds[i] else (100 - progresses[i])//speeds[i] for i in range(n) ]
    i, j = 0, 0
    while j < n:
        if day[i] >= day[j]:
            j += 1
        else:
            answer.append(j - i)
            i = j
    else:
        answer.append(j - i)
    return answer