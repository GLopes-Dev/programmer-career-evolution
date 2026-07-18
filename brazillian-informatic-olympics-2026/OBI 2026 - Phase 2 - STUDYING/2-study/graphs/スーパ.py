precos = {
    "banana": 3.50,
    "leite": 4.20,
    "pao": 2.00,
    "cafe": 8.50
}
compras = ["pao", "leite", "pao", "cafe", "banana"]
total = 0
for c in compras:
    total += precos[c]
print(f"{total:.2f}")
