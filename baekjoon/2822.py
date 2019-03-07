li = []
for i in range(1, 9):
    a = int(input())
    li.append([a, i])
li.sort(reverse = True)
pro = []
score = 0
for i in range(5):
    score += li[i][0]
    pro.append(li[i][1])
pro.sort()
print(score)
print(' '.join(map(str,pro)))