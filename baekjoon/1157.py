test = input()
cnt = [0]*26
for i in test:
    cnt[ord(i.upper()) - ord('A')] += 1
Max = max(cnt)
if cnt.count(Max) == 1:
    print(chr(cnt.index(Max) + ord('A')))
else:
    print('?')
