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