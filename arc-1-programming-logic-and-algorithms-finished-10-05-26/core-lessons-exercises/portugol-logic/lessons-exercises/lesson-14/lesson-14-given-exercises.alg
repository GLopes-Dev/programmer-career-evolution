algoritmo "FootballTournament"
var
    time: vetor[1..3] de caractere
    c, j: inteiro
inicio
    escreval("---------------------")
    escreval(" FOOTBALL TOURNAMENT ")
    escreval("---------------------")
    para c <- 1 ate 3 faca
        escreva("Team ", c, " Name: ")
        leia(time[c])
    fimpara

    limpatela
    escreval("-------------")
    escreval(" MATCHS LIST ")
    escreval("-------------")
    para c <- 1 ate 2 faca
        para j <- 1 ate 2 faca
            se (time[c] <> time[j]) entao
                escrevaL (time[c]:15, "[ ] X [ ] ", time[j])
            fimse
        fimpara
    fimpara
fimalgoritmo



// Gabarito: a, b, c, d, a
algoritmo "ExamCorrection"
var
    gab: vetor[1..5] de caractere
    exam: vetor[1..5] de caractere
    name: vetor[1..3] de caractere
    n: vetor[1..3] de real
    SM, med: real
    c, j: inteiro
inicio
    SM <- 0
    med <- 0
    escreval("STEP 1 - TEMPLATE REGISTER ")
    escreval("---------------------------")
    para c <- 1 ate 5 faca
        escreva("Question ", c, ": ")
        leia(gab[c])
    fimpara
    para c <- 1 ate 3 faca
        limpatela
        escreval("------------------------")
        escreval("STUDENT ", c)
        escreval("------------------------")
        escreva("Name: ")
        leia(name[c])
        para j <- 1 ate 5 faca
            escreva("Question ", j, ": ")
            leia(exam[j])
            se (exam[j] = gab[j]) entao
                n[c] <- n[c] + 2
                SM <- SM + 2
            fimse
        fimpara
    fimpara
    med <- SM/3
    limpatela
    escreval(" FINAL GRADES ")
    escreval("---------------------")
    para c <- 1 ate 3 faca
        escreval(name[c]:15, n[c]:3:1)
    fimpara
    escreval("---------------------")
    escreval("CLASS AVERAGE: ", med:3:1)
fimalgoritmo



































algoritmo "CinemaReservation"
var
    seats: vetor[1..10] de caractere
    seat, c: inteiro
    choice: caractere
inicio
    para c <- 1 ate 10 faca
        seats[c] <- "B" + numpcarac(c)
    fimpara
    repita
        para c <- 1 ate 10 faca
            escreva("[ ", seats[c], " ]")
        fimpara
        escreval("")
        escreval("--------------------------------------------------------")
        escreva("Which seat do you want to book: B")
        leia(seat)
        se (seats[seat] = "---") entao
            escreval("ERROR: Ocupied Seat")
        senao
            seats[seat] <- "---"
            escreval("Seat B", seat, " Booked!")
        fimse
        escreva("Continue? [S/N] ")
        leia(choice)
        limpatela
    ate (choice = "n") ou (choice = "N")
fimalgoritmo