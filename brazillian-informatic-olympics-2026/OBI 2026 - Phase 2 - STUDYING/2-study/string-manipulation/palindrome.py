def ispalindrom(word):
    wordinv = word[::-1]
    if wordinv == word:
        return True
    return False
word = input().lower()
print(ispalindrom(word))