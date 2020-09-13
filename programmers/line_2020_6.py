def solution(companies, applicants):
    answer = []
    companies = [i.split() for i in companies]
    applicants = [i.split() for i in applicants]
    companies = {i[0]:[i[1], int(i[2])]for i in companies}
    applicants = {i[0]:[i[1], int(i[2]), True]for i in applicants}
    entry = {i[0]:[]for i in companies}
    for _ in range(4):
        for i in applicants.keys():
            if applicants[i][1] and applicants[i][2]:
                entry[applicants[i][0][0]].append(i)
                applicants[i][0] = applicants[i][0][1:]
                applicants[i][1] -= 1
        for i in entry.keys():
            n = companies[i][1]
            for j in companies[i][0]:
                if j in entry[i]:
                    if n:
                        n -= 1
                        applicants[j][2] = False
                    else:
                        entry[i].remove(j)
                        applicants[j][2] = True
    for i in entry.keys():
        entry[i].sort()
    answer = [company+'_'+''.join(applicant) for company, applicant in entry.items()]
    return answer