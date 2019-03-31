n = int(input())
li = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    get = list(map(int, input().split()))
    if get[0] == 1:
        for i in range(get[1], get[2] + 1):
            li[i] ^= get[3]
    if get[0] == 2:
        ans = 0
        for i in range(get[1], get[2] + 1):
            ans ^= li[i]
        print(ans)