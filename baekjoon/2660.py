N = int(input())
li = [[] for _ in range(N + 1)]
ans_score = 50
result = []
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    li[a].append(b)
    li[b].append(a)
for i in range(1, N + 1):
    visit = [True] * (N + 1)
    visit[0] = False
    visit[i] = False
    que = [i]
    que_end = 1
    score = 0
    while True in visit:
        que_cnt = 0
        for j in range(que_end):
            for k in li[que[j]]:
                if visit[k]:
                    visit[k] = False
                    que.append(k)
                    que_cnt += 1
        que = que[que_end:]
        que_end = que_cnt
        score += 1
    if score < ans_score:
        ans_score = score
        result = [i]
    elif score == ans_score:
        result.append(i)
print(ans_score, len(result))
print(' '.join(map(str, result)))