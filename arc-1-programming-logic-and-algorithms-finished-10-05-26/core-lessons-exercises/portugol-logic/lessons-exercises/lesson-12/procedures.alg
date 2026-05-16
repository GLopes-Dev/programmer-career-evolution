algoritmo "Heavy"
var
    i: inteiro
    n, pesado: caractere
    p, mai: real
procedimento topo()
inicio
    limpatela
    escreval("------------------------------------")
    escreval(" D E T E C T O R   DE   P E S A D O ")
    escreval(" Maior Peso ate agora: ", mai, "Kg")
    escreval("------------------------------------")
fimprocedimento
inicio
    Topo()
    para i <- 1 ate 5 faca
        escreva("Digite o nome: ")
        leia (n)
        escreva("Digite o peso de ", n, ": ")
        leia(p)
        se (p>mai) entao
            mai <- p
            pesado <- n
        fimse
        Topo()
    fimpara
    Topo()
    escreval("A pessoa mais pesada foi ", pesado, " com ", mai, " quilos.") 
fimalgoritmo

////
algoritmo "SomaProcedimento"
var
    x, y: inteiro
procedimento soma(a, b: inteiro)
inicio
    escreval("Recebi o valor ", a)
    escreval("Recebi o valor ", b)
    escreval("A soma entre os dois e ", a + b)
fimprocedimento
inicio
    x <- 5
    y <- 3
    soma(x, y)
fimalgoritmo

///
algoritmo "EvenOrOddPrecedure"
var
    n: inteiro
procedimento EVOD(num: inteiro)
inicio
    se (num%2=0) entao
        escreva("The number is Even.")
    senao
        escreva("The number is Odd.")
    fimse
fimprocedimento
inicio
    escreva("Type a number: ")
    leia(n)
    EVOD(n)
fimalgoritmo



////

algoritmo "Soma"
var
    x, y: inteiro
procedimento Soma(var a, b: inteiro)
inicio
    a <- a + 1
    b <- b + 2
    escreval("Valor de A = ", a)
    escreval("Valor de B = ", b)
    escreval("A soma de A + B vale", a+b)
fimprocedimento
inicio
    x <- 4
    y <- 8
    Soma(x, y)
    escreval("Valor de X = ", x)
    escreval("Valor de Y = ", y)
fimalgoritmo


////

algoritmo "Fibonacci2.0"
var
    c, t1, t2, t3: inteiro
procedimento ProximoFibonacci(var a, b: inteiro)
var c: inteiro
inicio
    c <- a + b
    escreva(c)
    a <- b
    b <- c   
fimprocedimento
inicio
    t1 <- 0
    escreva(t1)
    t2 <- 1
    escreva(t2)
    para c <- 3 ate 10 faca
        ProximoFibonacci(T1, T2) 
    fimpara
fimalgoritmo