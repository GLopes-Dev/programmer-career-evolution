algoritmo "DissecandoMatrizes"
var
    m: vetor[1..4, 1..4] de inteiro
    l, c, option: inteiro

procedimento Menu()
inicio
    escreval("MENU DE OPÇÕES")
    escreval("====================")
    escreval("[1] Mostrar a Matriz")
    escreval("[2] Diagonal Principal")
    escreval("[3] Triangulo Superior")
    escreval("[4] Triangulo Inferior")
    escreval("[5] Sair")
    escreva("===== OPÇÃO: ")
    escreva()
    leia(option)
    escolha option
        caso 1
            limpatela
            Mat()
            Menu()
        caso 2
            limpatela
            Diag()
            Menu()
        caso 3
            limpatela
            TriSup()
            Menu()
        caso 4
            limpatela
            TriInf()
            Menu()
        caso 5
            interrompa
    fimescolha
fimprocedimento

procedimento Mat()
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            escreva(m[l, c]:5)
        fimpara
        escreval()
    fimpara
    escreval()
fimprocedimento

procedimento Diag()
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            se (l = c) entao
                escreva(m[l, c]:5)
            senao
                escreva("":5)
            fimse
        fimpara
        escreval()
    fimpara
    escreval()
fimprocedimento

procedimento TriSup()
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            se (c > l) entao
                escreva(m[l, c]:5)
            senao
                escreva("":5)
            fimse
        fimpara
        escreval()
    fimpara
    escreval()
fimprocedimento
procedimento TriInf()
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            se (l > c) entao
                escreva(m[l, c]:5)
            senao
                escreva("":5)
            fimse
        fimpara
        escreval()
    fimpara
    escreval()
fimprocedimento
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            escreva("Type the position [", l, ", ", c, "] value: ")
            leia(m[l, c])
        fimpara
    fimpara
    limpatela
    Menu()
    limpatela
    escreval("===================")
    escreval("Encerrando...")
    escreval("===================")
fimalgoritmo