algoritmo "Even"
var
    n: vetor[1..7] de inteiro
    c, totEven: inteiro
inicio
    totEven <- 0
    para c <- 1 ate 7 faca
        escreva("Number ", c, ": ")
        leia(n[c])
        se (n[c]%2=0) entao
            totEven <- totEven + 1
        fimse
    fimpara
    para c <- 1 ate 7 faca
        se (n[c]%2=0) entao
            totEven <- totEven + 1
            escreval("EVEN number in position ", c)
        fimse
    fimpara
    escreval("Total amount of EVEN numbers: ", totEven)
fimalgoritmo



algoritmo "ClassList"
var
    name: vetor[1..4] de caractere
    g1: vetor[1..4] de real
    g2: vetor[1..4] de real
    med: vetor[1..4] de real
    c, totAlunos: inteiro
    SM, MC: real
inicio
    para c <- 1 ate 4 faca
        escreval("Student ", c)
        escreva("Name: ")
        leia(name[c])
        escreva("First Grade: ")
        leia(g1[c])
        escreva("Second Grade: ")
        leia(g2[c])
        med[c] <- (g1[c] + g2[c]) / 2
        SM <- SM + med[c]
        limpatela
    fimpara
    MC <- SM/4
    limpatela
    escreval("  STUDENTS LIST  ")
    escreval("=================")
    escreval("Name":16, "AVG")
    para c <- 1 ate 4 faca
        escreval(name[c]:15, med[c]:4:1)
        se (med[c] > MC) entao
            totAlunos <- totAlunos + 1
        fimse
    fimpara
    escreval("-----------")
    escreval("Class Average: ", MC:4:1)
    escreval("Total Students over the Class Average: ", totAlunos)
fimalgoritmo



algoritmo "OnlyMatterWhoStartsWithC"
var
    nome: caractere
    soC: vetor[1..10] de caractere
    c, tot: inteiro
inicio
    tot <- 0
    para c <- 1 ate 10 faca
        escreva("Type your name: ")
        leia(name)
        se (Copia(maiusc(name, 1, 1)) = "C") entao
            tot <- tot + 1
            soC[tot] <- name
        fimse
    fimpara
    
    limpatela
    escreval("FINAL LIST")
    escreval("--------------")
    para c <- 1 ate tot faca
        escreval(soC[c])
    fimpara
fimalgoritmo



algoritmo "VectorOrder"
var
    vet: vetor[1..4] de inteiro
    c, j, aux: inteiro
inicio
    para c <- 1 ate 4 faca
        escreva("Type a number: ")
        leia(vet[c])
    fimpara

    para c <- 1 ate 3 faca
        para j <- (c + 1) ate 4 faca
            se (vet[c] > vet[j]) entao
                aux <- vet[c]
                vet[c] <- vet[j]
                vet[j] <- aux
            fimse        
        fimpara
    fimpara

    para c <- 1 ate 4 faca
        escreva("{", vet[c], "}")
    fimpara
fimalgoritmo