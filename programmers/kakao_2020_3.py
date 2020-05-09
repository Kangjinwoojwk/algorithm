
# 효율성 3개 케이스 틀리는 코드 흠...

def solution(gems):
    answer = []
    gemdict = {i:0 for i in gems}
    distance = 100000
    start, end = 0, 0
    gemdict[gems[end]] += 1
    end += 1
    while end < len(gems):
        if end - start < distance:
            if 0 in gemdict.values():
                gemdict[gems[end]] += 1
                end += 1
            else:
                distance = end - start
                answer = [start + 1, end]
                gemdict[gems[start]] -= 1
                start += 1
        else:
            gemdict[gems[start]] -= 1
            start += 1
    if not answer:
        answer = [1, len(gems)]
    return answer

# 보석 종류별로 다 사기 시간 초과 코드

def solution(gems):
    answer = []
    gemSet = set(gems)
    start, end = 0, 1
    distance = 100000
    def chk(table):
        for i in gemSet:
            if i not in table:
                return False
        return True
    while end <= len(gems):
        if chk(gems[start:end]):
            if end - start < distance:
                distance = end - start
                answer = [start + 1, end]
            start += 1
        else:
            end += 1
    return answer