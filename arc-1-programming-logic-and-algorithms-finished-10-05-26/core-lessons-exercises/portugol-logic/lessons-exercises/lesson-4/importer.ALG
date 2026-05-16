algoritmo "Importer"
var
   preco: real
   frete: real
   total1: real
   total2: real
   result: logico
inicio
   escreval("Inform the product price (R$): ")
   leia(preco)
   escreval("Inform the shipping cost (R$): ")
   leia(frete)
   total1 <- (0.6 * (preco + frete))
   total2 <- preco + frete + total1
   escreval("The total price is: ", total2)
   result <- (total2 = 1000) ou (total2 < 1000)
   escreval("Did the total fall below 1000? ", result)


fimalgoritmo