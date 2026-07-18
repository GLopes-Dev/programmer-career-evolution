def ispalindrom(word):
    wordinv = word[::-1]
    return wordinv == word
word = input().lower()
print(ispalindrom(word))