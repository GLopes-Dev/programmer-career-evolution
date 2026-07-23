S = input().strip()
vogais = set("aeiou")
consoantes = [char for char in S if char not in vogais]
consoantes_invertidas = consoantes[::-1]
resultado = "".join(consoantes_invertidas)
print(resultado)