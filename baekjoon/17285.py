data = input()
firstdata = 'CHICKENS'
key = int()
i = 0
while True:
    if ''.join([chr(ord(j) ^ i) for j in data[:8]]) == firstdata:
        key = i
        break
    i += 1
print(''.join([chr(ord(j) ^ key) for j in data]))