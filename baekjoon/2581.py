prime_number = [True] * 10001
prime_number[0] = prime_number[1] = False
for i in range(2, 101):
    if prime_number[i]:
        for j in range(i * 2, 10001, i):
            prime_number[j] = False
prime_number = [i for i in range(10001) if prime_number[i]]
M = int(input())
N = int(input())
ans1 = 0
ans2 = 0
for i in prime_number:
    if M <= i <= N:
        ans1 += i
        if ans2 == 0:
            ans2 = i
    if i > N:
        break
if ans2:
    print(ans1)
    print(ans2)
else:
    print(-1)