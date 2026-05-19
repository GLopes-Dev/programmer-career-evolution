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