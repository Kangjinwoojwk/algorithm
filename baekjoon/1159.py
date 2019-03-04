T = int(input())
input_data = ''.join([input()[0] for _ in range(T)])
result = ''.join([chr(i) for i in range(96, 123) if input_data.count(chr(i)) >= 5])
if result == '':
    result = 'PREDAJA'
print(result)