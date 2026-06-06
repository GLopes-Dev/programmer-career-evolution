phrase = 'CAKE'
inverted_sentence = ''

for i in range(len(phrase) - 1, -1, -1):
    inverted_sentence += phrase[i]
print(inverted_sentence)