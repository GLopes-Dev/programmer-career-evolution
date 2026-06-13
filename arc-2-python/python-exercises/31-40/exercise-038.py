#Challenge 038 - Make a program that reads two integers and compares them, displaying a message on the screen:
#The first value is greater
#The second value is greater
#The two values are equal

print('=' * 10, '[Challenge 038]', '=' * 10)
N1 = int(input('First Value: '))
N2 = int(input('Second Value: '))
if N1 > N2:
    print('The first value is greater.')
elif N2 > N1:
    print('The second value is greater.')
else:
    print('The two values are equal.')