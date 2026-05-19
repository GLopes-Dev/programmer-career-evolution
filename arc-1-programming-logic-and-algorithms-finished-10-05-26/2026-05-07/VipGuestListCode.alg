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