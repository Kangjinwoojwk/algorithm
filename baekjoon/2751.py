N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
print('\n'.join(map(str, li)))