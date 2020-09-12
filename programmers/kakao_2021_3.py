

# 효율성 미통과
def solution(info, query):
    answer = []
    language = ['cpp', 'java', 'python']
    job = ['backend', 'frontend']
    career = ['junior', 'senior']
    food = ['chicken', 'pizza']
    db = dict()
    for i in language:
        db[i] = dict()
        for j in job:
            db[i][j] = dict()
            for k in career:
                db[i][j][k] = dict()
                for l in food:
                    db[i][j][k][l] = list()

    def count_person(l, j, c, f, s):
        cnt = 0
        lang = []
        jo = []
        car = []
        foo = []
        if l == '-':
            lang = language
        else:
            lang.append(l)
        if j == '-':
            jo = job
        else:
            jo.append(j)
        if c == '-':
            car = career
        else:
            car.append(c)
        if f == '-':
            foo = food
        else:
            foo.append(f)
        for i in lang:
            for j in jo:
                for k in car:
                    for l in foo:
                        for m in db[i][j][k][l]:
                            if m >= s:
                                cnt += 1
        return cnt

    for i in info:
        l, j, c, f, score = i.split()
        db[l][j][c][f].append(int(score))
    for i in query:
        l, j, c, f = i.split(' and ')
        f, score = f.split()
        score = int(score)
        answer.append(count_person(l, j, c, f, score))

    return answer