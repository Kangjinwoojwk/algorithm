N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
di = {i:li.count(i) for i in set(li)}
m = 0
bin = []
for k, v in di.items():
    if v > m:
        m = v
for k, v in di.items():
    if v == m:
        bin.append(k)
print(int(round(sum(li)/N, 0)))
print(li[N//2])
if len(bin) > 1:
    print(bin[1])
else:
    print(bin[0])
print(max(li) - min(li))