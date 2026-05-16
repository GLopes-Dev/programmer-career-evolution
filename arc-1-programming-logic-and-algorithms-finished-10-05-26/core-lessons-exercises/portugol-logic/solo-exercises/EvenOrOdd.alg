algoritmo "Renshuu"
var
    num, usChoice: inteiro

funcao EvenOrOdd(n: inteiro): caractere
inicio
    se (n%2=0) entao
        retorne "Even"
    senao
        retorne "Odd"
    fimse
fimfuncao
inicio
    repita
        escreval("==================")
        escreval(" Even Or Odd Check ")
        escreval("===================")
        escreval("Type a number: ")
        leia(num)
        escreval("===================")
        escreval(EvenOrOdd(num))
        escreval("===================")
        escreval("[1] Continue")
        escreval("[2] Leave")
        leia(usChoice)
        limpatela
    ate (usChoice = 2)
    limpatela
    escreval("============")
    escreval("Leaving Program... Thank you!")
    escreval("============")
fimalgoritmo


//Option 2

algoritmo "Renshuu"
var
    num, usChoice: inteiro
    result: caractere
funcao EvenOrOdd(n: inteiro): caractere
inicio
    se (n%2=0) entao
        retorne "Even"
    senao
        retorne "Odd"
    fimse
fimfuncao
inicio
    repita
        escreval("==================")
        escreval(" Even Or Odd Check ")
        escreval("===================")
        escreval("Type a number: ")
        leia(num)
        escreval("===================")
        result <- EvenOrOdd(num)
        escreval(result)
        escreval("===================")
        escreval("[1] Continue")
        escreval("[2] Leave")
        leia(usChoice)
        limpatela
    ate (usChoice = 2)
    limpatela
    escreval("============")
    escreval("Leaving Program... Thank you!")
    escreval("============")
fimalgoritmo