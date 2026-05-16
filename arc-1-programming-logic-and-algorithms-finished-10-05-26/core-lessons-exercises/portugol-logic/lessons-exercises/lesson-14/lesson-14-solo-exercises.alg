algoritmo "BJJ Tournament Scout"
var
    weight: vetor[1..6] de real
    c, check, totWeight, totAthletes: inteiro
    maxWeight, aux, sMed, med: real
inicio
    totAthletes <- 0
    sMed <- 0
    med <- 0
    //Input
    para c <- 1 ate 6 faca
        escreval("BJJ TOURNAMENT SCOUT")
        escreval("====================")
        escreva("Athlete ", c, " Weight: ")
        leia(weight[c])
        totAthletes <- totAthletes + 1
        sMed <- sMed + weight[c]
        limpatela
    fimpara
    med <- sMed / totAthletes
    escreval("BJJ TOURNAMENT SCOUT")
    escreval("====================")
    escreva("What's the maximum weight for the Featherweight Category?")
    leia(maxWeight)
    //Ordenation
    para c <- 1 ate 5 faca
        para check <- (c + 1) ate 6 faca
            se (weight[c]) > (weight[check]) entao
                aux <- weight[c]
                weight[c] <- weight[check]
                weight[check] <- aux
            fimse
        fimpara
    fimpara
    //Filter and Output
    limpatela
    escreval("ATHLETES WEIGHT LIST")
    escreval("====================")
    escreval("Maximum Weight: ", maxWeight:3:1)
    para c <- 1 ate 6 faca
        se (weight[c] <= maxWeight) entao
            escreval("Athlete ", c, "   ", weight[c]:3:1, "Kg", "   Ideal Weight")
            totWeight <- totWeight + 1
        senao
            escreval("Athlete ", c, "   ", weight[c]:3:1, "Kg", "   Overweight")
        fimse
    fimpara
    escreval("Total Athletes who made the weight: ", totWeight)
    escreval("Average Weight of all registered Athletes: ", med:3:1)
fimalgoritmo

















algoritmo "Storage"
var
    drawers: vetor[1..5] de caractere
    object, choice: caractere
    c, drawer, drawerChoice: inteiro
inicio
    para c <- 1 ate 5 faca
        drawers[c] <- "----"
    fimpara

    repita
        para c <- 1 ate 5 faca
            escreval("[ Drawer ", c, " - (", drawers[c], ")]")
            escreval("=========================")
        fimpara
        escreva("What do you want to storage? ")
        leia(object)
        escreva("Which drawer do you want to storage ", object, "? Drawer: ")
        leia(drawer)
        escreval("===========================")
        se (drawers[drawer] <> "----"  ) entao
            escreval("Drawer ", drawer, " is full. Do you want do substitute it? ")
            escreval("[1] Yes")
            escreval("[2] No")
            leia(drawerChoice)
            se (drawerChoice = 1) entao
                drawers[drawer] <- object
                escreval(object, " stored in Drawer ", drawer)
            fimse
        senao
            drawers[drawer] <- object
            escreval(object, " stored in Drawer ", drawer)
        fimse
        escreval("Continue? [S/N]")
        leia(choice)
        limpatela
    ate (choice = "n") ou (choice = "N")
    para c <- 1 ate 5 faca
        escreval("[ Gaveta ", c, " - (", drawers[c], ")]")
        escreval("=========================")
    fimpara
fimalgoritmo
































algoritmo "VipGuestList"
var
    names: vetor[1..6] de caractere
    vip: vetor[1..6] de caractere
    name: caractere
    c, totVip, totNames: inteiro
inicio
    para c <- 1 ate 6 faca
        escreva("Type the ", c, " name: ")
        leia(name)
        se (Copia(Maiusc(name), 1, 1) = "A") entao
            totVip <- totVip + 1
            vip[totVip] <- name
        senao
            totNames <- totNames + 1
            names[totNames] <- name
        fimse
    fimpara
    limpatela

    escreval("USER'S LIST")
    escreval("===============")
    para c <- 1 ate 6 faca
        escreval("User ", c, "   ", names[c])
    fimpara
    escreval("===============")
    escreval("VIP'S LIST")
    escreval("===============")
    para c <- 1 ate 6 faca
        escreval("Vip ", c, "   ", vip[c])
    fimpara
fimalgoritmo








algoritmo "SurfScoreBoard"
var
    names: vetor[1..5] de caractere
    scores: vetor[1..5] de real
    bestName, AboveAvg, aux2: caractere
    bestScore, med, SM, aux: real
    c, j: inteiro
procedimento Menu()
inicio
    limpatela
    escreval("Score Registration")
    escreval("==================")
fimprocedimento
funcao Verify(var bS: real) : real
inicio
    se (scores[c] > bestScore) entao
        bestScore <- scores[c]
        bestName <- names[c]
    fimse
    retorne bestScore, bestName
fimfuncao
procedimento LeaderBoard()
inicio
    escreval("              LEADERBOARD             ")
    escreval("======================================")
    escreval("Winner: ", bestName)
    escreval("Score: ", bestScore)
    escreval("--------------------------------------")
    escreval("Classified Athletes (Score Higher than ", med,")")
    escreval("--------------------------------------")
    escreval("Name         Score")
    escreval("----          ---")
fimprocedimento
inicio
    bestScore <- 0
    med <- 0
    SM <- 0
    para c <- 1 ate 5 faca
        Menu()
        escreval("Athlete ", c)
        escreval("-----------")
        escreva("Name: ")
        leia(names[c])
        escreva("Score: ")
        leia(scores[c])
        SM <- SM + scores[c]
        bestScore <- Verify(bestScore)
    fimpara
    med <- SM/5
    para c <- 1 ate 4 faca
        para j <- c+1 ate 5 faca
           se (scores[c] < scores[j]) entao
               aux <- scores[c]
               aux2 <- names[c]
               scores[c] <- scores[j]
               names[c] <- names[j]
               scores[j] <- aux
               names[j] <- aux2
           fimse
        fimpara
    fimpara
    limpatela
    LeaderBoard()
    para c <- 1 ate 5 faca
        se ((scores[c] >= med) e (scores[c] <> bestScore)) entao
           escreval(names[c]:14, scores[c])
        fimse
    fimpara
fimalgoritmo











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