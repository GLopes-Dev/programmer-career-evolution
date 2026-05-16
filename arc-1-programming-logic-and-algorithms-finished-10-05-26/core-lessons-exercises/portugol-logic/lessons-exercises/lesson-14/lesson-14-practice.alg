algoritmo "Vectors"
var
    n: vetor[1..4] de inteiro
    choice: caractere
inicio
    escreval("Type a number: ")
    leia(n[1])
    escreval("Type another number: ")
    leia(n[2])
    escreval("Another number: ")
    leia(n[3])
    escreval("Another number: ")
    leia(n[4])
    escreval("Numbers registred. Want to see the registrated numbers list? ")
    escreval("[1] Yes")
    escreval("[2] No")
    leia(choice)
    se (choice = 1) entao
        limpatela
        escreval(n[1..4])
    fimse
fimalgoritmo


algoritmo "TesteVetor"
var
    v: vetor[1..6] de inteiro
    c: inteiro 
inicio
    para c <- 1 ate 6 faca
        escreva("Digite o ", c, "o . valor: ")
        leia(v[c])
    fimpara
    para c <- 1 ate 6 faca
        escreva ("{", v[c], "}")
    fimpara
fimalgoritmo





algoritmo "Even"
var
    n: vetor [1..7] de inteiro
    c, totEven, totOdd: inteiro
inicio
    totEven <- 0
    totOdd <- 0
    para c <- 1 ate 7 faca
        escreval("Number ", c, ": ")
        leia(n[c])
    fimpara
    para c <- 1 ate 7 faca
        se (n[c]%2=0) entao
            totEven <- totEven + 1
            escreval("Even number in ", c, "º position.")
        senao
            totOdd <- totOdd + 1
            escreval("Odd number in ", c, "º position.")
        fimse
    fimpara
    escreval("The total even numbers is: ", totEven)
    escreval("The total odd numbers is: ", totOdd)
fimalgoritmo


algoritmo "Even"
var
    n: vetor [1..7] de inteiro
    c, totEven: inteiro
inicio
    para c <- 1 ate 7 faca
        escreval("Number ", c, ": ")
        leia(n[c])
    fimpara
    para c <- 1 ate 7 faca
        se (n[c]%2=0) entao
            totEven <- totEven + 1
            escreval("Even number in ", c, "º position.")
        fimse
    fimpara
    escreval("The total even numbers is: ", totEven)
fimalgoritmo


algoritmo "TurmList"
var
    name: vetor[1..4] de caractere
    n1: vetor[1..4] de real
    n2: vetor[1..4] de real
    med: vetor[1..4] de real
    c: inteiro  
inicio
    para c <- 1 ate 4 faca
        escreval("Student ", c)
        escreva("Name: ")
        leia(name[c])
        escreva("First grade: ")
        leia(n1[c])
        escreva("Second grade: ")
        leia(n2[c])
        med[c] <- (n1[c] + n2[c]) / 2
    fimpara
    limpatela
    escreval("STUDENTS LIST")
    escreval("-------------")
    para c <- 1 ate 4 faca
        se (med[c] >= 5.0) entao
            escreval(name[c]:10, med[c]:4:1, "   Approved")
        senao
            escreval(name[c]:10, med[c]:4:1, "   Failed")
        fimse
    fimpara
fimalgoritmo








































algoritmo "OnlyMattersWhoStartWithC"
var
    name: vetor [1..7] de caractere
    name1: caractere
    c, tot: inteiro
inicio
    tot <- 0
    para c <- 1 ate 7 faca
        escreval("Name ", c)
        leia(name1)
        se (copia(maiusc(name1), 1, 1) = "C") entao
           tot <- tot + name1
           name1[tot] <- name1
        fimse
    fimpara

    limpatela
    escreval(" NAME WHO MATTERS LIST ")
    escreval("=======================")
    para c <- 1 ate tot faca
        escreval(name[c])
    fimpara
fimalgoritmo


algoritmo "OrdenaVetor"
var
    vet: vetor[1..4] de inteiro
    i, j, aux: inteiro
inicio
    para i <- 1 ate 4 faca
        escreva("Type a value: ")
        leia(vet[i])
    fimpara
    para i <- 1 ate 3 faca
        para j <- i+1 ate 4 faca
            se(vet[i] > vet[j]) entao
                aux <- vet[i]
                vet[i] <- vet[j]
                vet[j] <- aux
            fimse
        fimpara  
    fimpara

    para i <- 1 ate 4 faca
        escreva("{", vet[i], "}")
    fimpara
fimalgoritmo