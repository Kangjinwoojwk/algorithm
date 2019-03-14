cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()
for i in range(8):
    n = n.replace(cro[i], '0')
print(len(n))