phrase = 'Course in Video Python'
print(phrase)
print(phrase.upper().count('o'))

print(phrase.split(),'-'.join(phrase))

print(len(phrase))

print(len(phrase.strip()))

print(phrase.replace('Python', 'JavaScript'))
print(phrase.replace('Python', 'C++'))
print(phrase.replace('Course in Video Python', 'Computer Science Tokyo University from MEXT'))
phrase.replace('Python', 'Java')
print(phrase)
phrase = phrase.replace('Python', 'MySQL')
print(phrase)
phrase = phrase.replace('MySQL', 'Python')

print(phrase.split()[2])
print(phrase.split()[2][0:5])
print(phrase.split()[2][0:5:2])
print(phrase.split()[2], '-'.join(phrase))
print(len(phrase.split()[1]))