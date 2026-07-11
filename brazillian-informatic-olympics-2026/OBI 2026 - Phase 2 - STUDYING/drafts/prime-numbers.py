import math

def eh_primo(num):
    if num <= 1:
        return False
    raiz = int(math.sqrt(num))
    for i in range(2, raiz + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
if eh_primo(n):
    print("Primo")
else:
    print("Not prime")