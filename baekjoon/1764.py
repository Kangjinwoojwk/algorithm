N, M = map(int, input().split())
dud = set()
for i in range(N):
    dud.add(input())
result = []
for i in range(M):
    a = input()
    if a in dud:
        result.append(a)
result.sort()
print(len(result))
print('\n'.join(result))