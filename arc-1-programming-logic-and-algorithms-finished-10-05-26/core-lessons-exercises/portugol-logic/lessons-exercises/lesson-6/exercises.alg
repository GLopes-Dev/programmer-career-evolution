//Code for exercise 1 and 2 of lesson 6

algoritmo "Creuza01"
var
  ano_atual: inteiro
  ano_nasc: inteiro
  idade: inteiro
inicio
            escreval("What year is it? ")
            leia(ano_atual)
             escreval("In what year was I born? ")
             leia(ano_nasc)
             idade <- ano_atual - ano_nasc
              escreval("My age is ", idade)
fimalgoritmo


//////exercicio2/////////

algoritmo "Convert Reais to Dollars"
var
    reais: real
    dolares: real
inicio
            escreva("How many Reais do I have? ")
            leia(reais)
            dolares <- reais / 4.98
            escreva("I can have U$", dolares:5:2, " dollars.")
fimalgoritmo


//////////////