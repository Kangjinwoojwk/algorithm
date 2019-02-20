str1 = 'abcddcba'
cnt = len(str1) // 2
isPalindrome = True
for i in range(cnt):
    if str1[i] != str1[len[str1] -1 -i]:
        isPalindrome = False
        break
print(isPalindrome)