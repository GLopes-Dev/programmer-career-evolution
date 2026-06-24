import sys

matriz = [
    ["水-1", "来-2", "人-1"],
    ["行-2", "上-1", "下-1"],
    ["帰-2", "口-1", "車-2"]
]

nivel = int(input('Digite o nível que quer buscar: '))

for l in range(3):
    for c in range(3):
        item = matriz[l][c].split('-')
        if int(item[1]) == nivel:
            print(f'Kanji {item[0]} encontrado na posição [{l}][{c}]')
            