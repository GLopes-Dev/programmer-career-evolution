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












algoritmo "Tic-Tac-Toe"
var
    tab: vetor[1..3, 1..3] de caractere
    l, c, cont, rodadas: inteiro
    jogada, letter, error: caractere
    vitoria, jogada_valida, encontrou: logico
procedimento Tabuleiro()
inicio
    limpatela
    para l <- 1 ate 3 faca
        escreval("---+---+---+---")
        para c <- 1 ate 3 faca
        escreva("| ", tab[l, c], " |")
        fimpara
        escreval()
    fimpara
    escreval("---+---+---+---")
    escreval("==============")
    escreval(error)
fimprocedimento
procedimento TabInput(var jog: caractere)
inicio
    encontrou <- falso
    para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
            se (tab[l, c] = jog) entao
                encontrou <- verdadeiro
                tab[l, c] <- letter
                jogada_valida <- verdadeiro
            fimse
        fimpara
    fimpara
    se (encontrou = falso) entao
        error <- "POSIÇÃO INVALIDA OU JÁ OCUPADA!"
        jogada_valida <- falso
    fimse
fimprocedimento
procedimento CheckWin()
inicio
    se (tab[1,1] = letter) e (tab[1,2] = letter) e (tab[1,3] = letter) entao
        vitoria <- verdadeiro
    senao
        se (tab[2,1] = letter) e (tab[2,2] = letter) e (tab[2,3] = letter) entao
            vitoria <- verdadeiro
        senao
            se (tab[3,1] = letter) e (tab[3,2] = letter) e (tab[3,3] = letter) entao
                vitoria <- verdadeiro
            senao
                se (tab[1,1] = letter) e (tab[2,1] = letter) e (tab[3,1] = letter) entao
                    vitoria <- verdadeiro
                senao
                    se (tab[1,2] = letter) e (tab[2,2] = letter) e (tab[3,2] = letter) entao
                        vitoria <- verdadeiro
                    senao
                        se (tab[1,3] = letter) e (tab[2,3] = letter) e (tab[3,3] = letter) entao
                            vitoria <- verdadeiro
                        senao
                            se (tab[1,1] = letter) e (tab[2,2] = letter) e (tab[3,3] = letter) entao
                                vitoria <- verdadeiro
                            senao
                                se (tab[1,3] = letter) e (tab[2,2] = letter) e (tab[3,1] = letter) entao
                                    vitoria <- verdadeiro
                                fimse
                            fimse
                        fimse
                    fimse
                fimse
            fimse
        fimse
    fimse
fimprocedimento

inicio
    jogada_valida <- falso
    rodadas <- 0
    cont <- 1
    letter <- "X"
    vitoria <- falso
    para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
            tab[l, c] <- Numpcarac(cont)
            cont <- cont + 1
        fimpara
    fimpara
    repita
        Tabuleiro()
        escreva("Vai jogar [", letter, "] em qual posição? ")
        leia(jogada)
        TabInput(jogada)
        se (jogada_valida = verdadeiro) entao
            rodadas <- rodadas + 1
            CheckWin()
            se (vitoria = falso) entao
                se (letter = "X") entao
                    letter <- "O"
                senao
                    letter <- "X"
                fimse
            fimse
        fimse
    ate ((vitoria = verdadeiro) ou (rodadas = 9))
    Tabuleiro()
    escreval("==================")
    escreval("JOGO FINALIZADO!")
    se (vitoria = verdadeiro) entao
        escreval("O JOGADOR [", letter, "] VENCEU!")
    senao
        escreval("DEU VELHA! Ninguém venceu. ")
    fimse
fimalgoritmo







