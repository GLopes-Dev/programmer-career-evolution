algoritmo "Playlist"
var
    musics: vetor[1..20] de caractere
    c: inteiro
    totMusic: inteiro

procedimento Menu(var tot: inteiro)
var
    option, op: inteiro
inicio
    repita
        limpatela
        escreval(" WELCOME TO MUSIC PLAYER")
        escreval("=========================")
        escreval("[1] Open Playlist")
        escreval("[2] Add Musics to Playlist")
        escreval("[3] Leave")
        escreval("-------------------------")
        escreval("Select Option: ")
        repita
            leia(option)
            se ((option < 1) ou (option > 3)) entao
                escreva("Invalid Option. Try again: ")
            fimse
        ate ((option >= 1) e (option <= 3))
        escolha option
            caso 1
                se (totMusic = 0) entao
                    limpatela
                    escreval("Can't open Playlist (No musics in Playlist)")
                    escreval("------------")
                    escreval("Back...")
                    leia(op)
                senao
                    Playlist()
                fimse
            caso 2
                AddMusic(tot)
        fimescolha
    ate (option = 3)
fimprocedimento

procedimento Playlist()
var
 c, option: inteiro

inicio
    limpatela
    escreval(" PLAYLIST MENU ")
    escreval("===============")
    para c <- 1 ate totMusic faca
        escreval(c, " - ", musics[c])
    fimpara
    escreval("---------------")
    escreval("[4] Back...")
    leia(option)
fimprocedimento

procedimento AddMusic(var tot: inteiro)
var
    name: caractere
    option, c: inteiro
inicio
        para c <- 1 ate 20 faca
            limpatela
            escreval("ADD MUSIC TO PLAYLIST")
            escreval("=====================")
            escreval("Music Name: ")
            leia(name)
            totMusic <- totMusic + 1
            musics[totMusic] <- name
            escreval("----------------")
            escreval("Music added in Playlist")
            escreval("----------------")
            escreval("[1] Continue")
            escreval("[2] Back...")
            escreval("================")
            leia(option)
            se (option = 2) entao
               interrompa
            fimse
        fimpara
fimprocedimento

inicio
    totMusic <- 0
    para c <- 1 ate 20 faca
        musics[c] <- "----"
    fimpara
    Menu(totMusic)
    limpatela
    escreval("====================================")
    escreval("Leaving Music Player.... Thank you! ")
    escreval("====================================")
fimalgoritmo