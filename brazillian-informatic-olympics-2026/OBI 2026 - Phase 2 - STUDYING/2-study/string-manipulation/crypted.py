sentence = input().lower().replace(" ", "")
quantidade = []
for letra in set(sentence):
    qtd = sentence.count(letra)
    quantidade.append((letra, qtd))
quantidade_ordenada = sorted(quantidade, key=lambda x: (-x[1], x[0]))
print(*(quantidade_ordenada[0]))
