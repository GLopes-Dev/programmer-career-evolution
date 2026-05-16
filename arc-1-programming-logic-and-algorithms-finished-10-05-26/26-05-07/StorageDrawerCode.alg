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