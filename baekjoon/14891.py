def sol(number, direction):
    if number + 1 < 4 and visit[number + 1] and data[number][2] != data[number + 1][6]:
        visit[number + 1] = False
        sol(number + 1, -direction)
    if number - 1 >= 0 and visit[number -1] and data[number][6] != data[number - 1][2]:
        visit[number - 1] = False
        sol(number - 1, -direction)
    if direction == 1:
        data[number] = data[number][-1:] + data[number][0:-1]
    if direction == -1:
        data[number] = data[number][1:]+data[number][:1]
data = [list(map(int, list(input()))) for _ in range(4)]
n = int(input())
for i in range(n):
    visit = [True] * 4
    number, direction = map(int, input().split())
    visit[number - 1] = False
    sol(number - 1, direction)
j = 1
ans = 0
for i in data:
    ans += j * i[0]
    j *= 2
print(ans)