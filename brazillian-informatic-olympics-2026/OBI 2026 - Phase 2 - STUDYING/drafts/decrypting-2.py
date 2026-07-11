encrypted_text = 'pqtjwv'
size = -len(encrypted_text)

for l in range(-1, size-1, -1):
    letra = encrypted_text[l]
    letra = chr(ord(letra) - 2)
    print(letra, end="")
    