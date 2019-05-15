memo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
for i in range(10, 1001):
    memo.append(memo[i - 1] + memo[i - 2])
print(memo[int(input())]%10007)