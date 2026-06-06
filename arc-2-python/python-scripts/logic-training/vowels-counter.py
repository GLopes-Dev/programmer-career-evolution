phrase = str(input()).lower()
vow = 0
for letter in phrase:
    if letter in 'aeiou':
        vow += 1
print(vow)