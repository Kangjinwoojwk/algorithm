ans = list()
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        ans.pop()
    else:
        ans.append(a)
print(sum(ans))