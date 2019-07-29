import sys
N = int(sys.stdin.readline())
worker = set()
for _ in range(N):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        worker.add(a)
    elif b == 'leave':
        worker.remove(a)
worker = list(worker)
worker.sort(reverse=True)
print('\n'.join(worker))