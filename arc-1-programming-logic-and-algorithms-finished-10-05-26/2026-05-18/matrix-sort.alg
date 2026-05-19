Algoritmo "semnome"
var
    n: vetor[1..4, 1..4] de inteiro
    l, c, l2, c2, aux: inteiro
Inicio
      escreval("Hello, World!")
      para l de 1 ate 4 faca
           para c de 1 ate 4 faca
                escreva("Type the [", l, ", ", c, "] number:")
                leia(n[l, c])
           fimpara
      fimpara
      
      //Sort

      para l de 1 ate 4 faca
           para c de 1 ate 4 faca
                para l2 de 1 ate 4 faca
                     para c2 de 1 ate 4 faca
                          se n[l, c] < n[l2, c2] entao
                             aux <- n[l, c]
                             n[l, c] <- n[l2, c2]
                             n[l2, c2] <- aux
                          fimse
                     fimpara
                fimpara
           fimpara
      fimpara
      
      escreval("The numbers order is")
      para l de 1 ate 4 faca
           para c de 1 ate 4 faca
                escreva("[", n[l, c], "]":2)
           fimpara
           escreval()
      fimpara
Fimalgoritmo