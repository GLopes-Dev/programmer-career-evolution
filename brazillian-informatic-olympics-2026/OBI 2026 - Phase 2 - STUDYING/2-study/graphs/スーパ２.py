compras = ["pao", "leite", "pao", "cafe", "banana", "leite", "pao"]
quantidade = {}
for c in compras:
    if c in quantidade:
        quantidade[c] += 1
    else:
        quantidade[c] = 1
print(quantidade)