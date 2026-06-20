#Desafio 004 - Create a program that read something from the keyboard and show in the screen it's primitive type and all the possible informations about it

print('=========[Challenge 004]=========')
v = input('Type something: ')

print('Primitive Type: ', type(v))
print('Does it only have numbers? {}'.format(v.isnumeric()))
print('Does it only have letters? {}'.format(v.isalpha()))
print('Does it has letters or numbers? {}'.format(v.isalnum()))
print('Does it only have Uppercase letters? {}'.format(v.isupper()))
print('Does it only have Lowercase letters? {}'.format(v.islower()))