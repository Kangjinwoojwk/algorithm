N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li.sort()
print('\n'.join(map(str, li)))