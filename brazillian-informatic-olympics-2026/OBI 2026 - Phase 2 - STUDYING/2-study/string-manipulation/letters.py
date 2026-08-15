L = input()
palavras = input().split()
qtd = 0
for p in palavras:
    if L in p:
        qtd += 1

print(f"{(qtd / len(palavras)) * 100:.1f}")