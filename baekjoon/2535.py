N = int(input())
li = []
for _ in range(N):
    a, b, c = map(int, input().split())
    li.append([c, a, b])
li.sort(reverse=True)
print(li[0][1], li[0][2])
print(li[1][1], li[1][2])
if li[0][1] == li[1][1]:
    for i in range(2, N):
        if li[i][1] != li[0][1]:
            print(li[i][1], li[i][2])
            break
else:
    print(li[2][1], li[2][2])