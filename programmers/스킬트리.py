def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        chk = 0
        for j in i:
            if j in skill:
                if j == skill[chk]:
                    chk += 1
                else:
                    break
            else:
                continue
        else:
            answer += 1
    return answer