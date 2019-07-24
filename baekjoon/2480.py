data = list(map(int, input().split()))
data.sort()
if data[0] == data[1] == data[2]:
    print('1'+str(data[0])+'000')
elif data[0] == data[1]:
    print('1' + str(data[1]) + '00')
elif data[1] == data[2]:
    print('1' + str(data[1]) + '00')
else:
    print(data[2]*100)