import datetime
a = datetime.datetime.now()
month = ''
if a.month < 10:
    month = '0' + str(a.month)
else:
    month = a.month
print('{}-{}-{}'.format(a.year, month, a.day))