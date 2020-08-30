def solution(priorities, location):
    answer = 0
    chk = [0] * len(priorities)
    chk[location] = 1
    while True:
        get_file = priorities.pop(0)
        get_it = chk.pop(0)
        if not priorities or get_file >= max(priorities):
            answer += 1
            if get_it:
                break
            continue
        else:
            priorities.append(get_file)
            chk.append(get_it)
    return answer