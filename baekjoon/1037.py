cnt = int(input())
li = list(map(int, input().split()))
li.sort()
if cnt == 1:
    print(li[0] ** 2)
else:
    print(li[0] * li[-1])