//O que o seu código tem que fazer (o "job" dele):

//Ser um assistente de recepção: Ele deve ficar aberto e disponível para receber dados enquanto houver gente na fila.

//Identificar o atleta: Receber o nome e o peso.

//Ser o "Juiz de Mesa": Automaticamente olhar o peso e dizer: "Você vai lutar na categoria Pena" ou "Você é Pesadíssimo". O usuário não precisa pensar, o código decide.

//Ser o "Caixa": Se o cara for federado, o código já calcula o valor com 10% de desconto na hora.

//Gerar um relatório: No final de cada inscrição, ele mostra o "ticket" pronto com Nome, Peso, Categoria e Preço.

//Saber a hora de fechar: Quando você digitar "SAIR", ele encerra o expediente e diz quantos atletas foram inscritos no total.

//"Esqueleto" da Lógica (Fluxograma Mental)
//Para o seu cérebro de programador, o fluxo é esse:

//Início

//Loop (Enquanto): Tem mais alguém na fila?

//Entrada: Qual seu nome e peso?

//Processamento 1 (Se/Senao): Peso < 70? Categoria = Pena.

//Processamento 2 (Escolha Caso): É federado? Valor = 100 * 0.9.

//Saída: "Atleta [Nome] inscrito na categoria [Pena] por R$[90]."

//Fim do Loop

//Saída Final: "Total de inscritos hoje: [Contador]."

//Considerando: Inscriçao = R$100,00, se for federado, 100 * 10 / 100


algoritmo "OrganizaçãoJiu-Jitsu"
var
    name, category: caractere
    count, regisType: inteiro
    weight, price, discount: real
inicio
    escreval(" -------------------------------")
    escreval("|   Championship Registrations   |")
    escreval(" -------------------------------")
    escreval("Type the Athlete Name, Weight and Registration type")
    escreval("Type [Exit] to finish registrations. ")
    count <- 1
    enquanto (name <> "Exit") faca
        escreval("--------------------")
        escreval("Athlete ", count)
        escreva("Name: ")
        leia(name)
        se (name <> "Exit") entao
            escreva("Weight: ")
            leia(weight)
            escreval("Registration Type: ")
            escreval("[1] for Normal")
            escreval("[2] for Federate")
            escreval("[3] for Social")
            leia(regisType)
            se (weight < 64) entao
                category <- "Pluma"
            senao
                se (weight >= 64) e (weight < 76) entao
                category <- "Light"
                senao
                    se (weight >= 76) e (weight < 88) entao
                    category <- "Medium"
                    senao
                    category <- "Heavy"
                    fimse
                fimse
            fimse
            escolha (regisType) caso
            caso 1
                price <- 100
            caso 2
                discount <- (100 * 10) / 100
                price <- 100 - discount
            caso 3
                price <- 0
            outrocaso
                escreval("Invalid option.")
            fimescolha
            escreval("-----------------")
            escreval("The Athlete ", name, " from ", category, " category needs to pay R$",price)
            count <- count + 1
        fimse
    fimenquanto
    escreval("------------------------------------------------")
    escreval("  Registrations closed. Total Athletes:  ", count - 1)
fimalgoritmo
























//backup

algoritmo "OrganizaçãoJiu-Jitsu"
var
    name, category: caractere
    count, regisType: inteiro
    weight, price, discount: real
inicio
    escreval(" -------------------------------")
    escreval("|   Championship Registrations   |")
    escreval(" -------------------------------")
    escreval("Type the Athlete Name, Weight and Registration type")
    escreval("Type [Exit] to finish registrations. ")
    count <- 1
    enquanto (name <> "Exit") faca
        escreval("--------------------")
        escreval("Athlete ", count)
        escreva("Name: ")
        leia(name)
        escreva("Weight: ")
        leia(weight)
        escreval("Registration Type: ")
        escreval("[1] for Normal")
        escreval("[2] for Federate")
        escreval("[3] for Social")
        leia(regisType)
        se (weight < 64) entao
            category <- "Pluma"
        senao
            se (weight >= 64) e (weight < 76) entao
                category <- "Light"
            senao
                se (weight >= 76) e (weight < 88) entao
                    category <- "Medium"
                senao
                    category <- "Heavy"
                fimse
            fimse
        fimse
        escolha (regisType) caso
        caso 1
            price <- 100
        caso 2
            discount <- (100 * 10) / 100
            price <- 100 - discount 
        caso 3
            price <- 0
        outrocaso
            escreval("Invalid option.") 
        fimescolha
        escreval("-----------------")
        escreval("The Athlete ", name, " from ", category, " category needs to pay R$",price)
        count <- count + 1
    fimenquanto
    escreval("------------------------------------------------")
    escreval("  Registrations closed. Total Athletes:  ", count)
fimalgoritmo