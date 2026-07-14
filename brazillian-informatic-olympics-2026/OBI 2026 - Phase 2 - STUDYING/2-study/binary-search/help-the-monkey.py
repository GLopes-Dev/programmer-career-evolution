alturas = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
def binary(alturas, alvo):
    ini = 0
    fim = len(alturas) - 1
    resposta = -1

    while ini <= fim:
        meio = (ini + fim) // 2
        if alturas[meio] == alvo:
            return meio
        elif alturas[meio] < alvo:
            ini = meio + 1
        else:
            resposta = meio
            fim = meio - 1
        
    return resposta
print(binary(alturas, 51))



# [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# ini = 0
# fim = 9
# resposta = -1

# 1 Loop 
# [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
#  0  1  2  3   4   5   6   7   8    9
# meio = 4
# 16 == 15? False
# 16 < 15? False
# 16 > 15? True
# resposta = 4
# fim = 3

# 2 Loop  
# [2, 5, 8, 12]
#  0  1  2   3
# ini = 0
# fim = 3
# resposta = 4
# meio = 1
# 5 == 15? False
# 5 < 15? True
# ini = 2
# [8, 12]
#  2  3
# ini = 2
# fim = 3
# resposta = 4
# meio = 2
# 8 == 15? False
# 8 < 15? True
# ini = 3
# [12]
#  3
# ini = 3
# fim = 3
# resposta = 4
# meio = 3
# 3 == 15? False
# 3 < 15? True
# ini = 4
# fim do loop 4 > 3

# resumo:
# ini = 4
# fim = 3
# meio = 3
# resposta = 4

