n1 = float(input('First Grade: '))
n2 = float(input('Second Grade: '))
avg = (n1 + n2) / 2
if avg >= 7:
    print('Approved')
elif avg >= 5 and avg <= 6.9:
    print('Recovery')
else:
    print('Failed6.')