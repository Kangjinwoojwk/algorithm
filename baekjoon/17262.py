n = int(input())
go, come = 100000, 1
for i in range(n):
    s, e = map(int, input().split())
    if come < s:
        come = s
    if go > e:
        go = e
if go > come:
    print(0)
else:
    print(come - go)