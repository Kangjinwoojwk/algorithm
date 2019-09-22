a, b = map(int, input().strip().split(' '))
consumer = [0] * b
for _ in range(a):
    consumer[consumer.index(min(consumer))] += int(input())
print(max(consumer))