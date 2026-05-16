Algoritmos são conjuntos de passos finitos e organizados que, quando executados, resolvem um determinado problema.



Proporção Aúrea

''Phi'' = 1,618 (Não é PI)



Variáveis (Portugol)



identificador: tipo



Regras do identificador:

1 - Deve começar com uma letra

2 - Os próximos podem ser letras ou números

3 - Não pode utilizar nenhum símbolo, exceto \_

4 - Não deve haver espaços em branco.

5 - Não deve conter letras acentuadas nem acentos

6 - Não pode ser uma palavra reservada (palavras em azul no código)





&#x20;

Tipos Primitivos:



Inteiro: 1, -3, 258, -598, etc.

Real: 1.3   -384.93   98.2  3.1114

Caractere: "Gabriel" "1234" (Tudo que está entre aspas)

Logico: verdadeiro ou falso



Atribuições:



msg <- "Olá, Mundo!"



Símbolo de atribuição: <-



Comandos de Saída:



Escreva ("msg")

Escreva (msg)

Escreval ("msg")

Escreva ("mensagem", msg)





Observações:



Comando Escreva ("vazio"), escreve e mostra no prompt o que foi digitado dentro dos parênteses.



Comando Escreval ("vazio"), escreve e mostra no prompt o que foi digitado dentro do parênteses, mas escreve na linha abaixo.



Para escrever uma variável que você atribuiu, por exemplo: msg <- "Olá, Mundo!", eu atribui o caractere "Olá, Mundo!" ao identificador "msg"



Se eu quiser mostrar um identificador no prompt com o Escreva ou Escreval, não devo utilizar os aspas dentro dos parêntes: Escreva ("nome do identificador"), se não aparecerá somente o que você escreveu dentro das aspas, sempre que tiver aspas só aparecerá o que você escreveu nela.



Para aparecer o tipo que foi atribuído ao identificador, devo escrever: Escreva (nome do identificador), sem as aspas, somente com os parênteses e aparecerá o tipo que foi atribuído ao identificador (inteiro, real, caractere ou logica)





Comandos de Entrada:

Leia





Operadores aritméticos:

\+ Adição (A + B)

\- Subtração (A - B)

\* Multiplicação (A \* B)

/ Divisão (A / B)

\\ Divisão Inteira ( A \\ B)

^ Exponenciação (A ^ B)

% Módulo (A % B)



Ordem de precedência (mais prioridade nas operações):



() parênteses, prioridade máxima

^ exponenciação, segunda prioridade

\* e / multiplicação e divisão, terceira prioridade

\+ e - adição e subtração, ultima prioridade



Funções aritméticas:

Abs (Valor Absoluto) | Ex: Abs(-10) = 10

Exp (Exponenciação)  | Ex: Exp(3,2) = 9  (A vírgula entre o 3 e o 2 significa a exponenciação.)

Int (Valor Inteiro)  | Ex: Int(3.9) = 3

RaizQ (Raiz Quadrada)| Ex: RaizQ(25) = 5

Pi (Retorna Pi)      | Ex:Pi = 3.14...

Sen (Seno "rad")     | Ex: Sen(0.523) = 0.5

Cos (Cosseno "rad")  | Ex: Cos(0.523) = 0.86

Tan (Tangente "rad") | Ex: Tan(0.523) = 0.57

GraupRad (Graus para Rad) | Ex: GraupRad(30) = 0.52





Operadores Relacionais:

> (Maior que)

< (Menor que)

>= (Maior ou igual a)

<= (Menor ou igual a)

= (Igual a)

<> (Diferente de)



Operadores Lógicos:



Operador E

p | q | p E q |      V e V = V

V | V |   V   |      V e F = F

V | F |   F   |      F e F = F

F | V |   F   |

F | F |   F   |      OBS: No operador E os dois tem que ser verdadeiro, se não, é falso.



Operador OU

p | q | p OU q|     Um dos dois tem q ser verdadeiro pelo menos.

V | V |   V   |     V e V = V

V | F |   V   |     V e F = V

F | V |   V   |     F e V = V

F | F |   F   |     F e F = F



Operador NAO

p | NAO p|     Se for V, é falso

V |  F   |     Se for F, é verdadeiro

F |  V   |





Para utilizar operadores lógicos, só pode testar valores lógicos.

Todas as expressões utilizando os operadores relacionais geram resultados lógicos.





OBS: Muito importante em geral



Cada conta especifica tem q ter seu próprio parênteses



Ordem de precedência geral:



Numa expressão que tenha operadores aritméticos, lógicos e relacionais ao mesmo tempo



Serão realizada as operações aritméticas primeiro (prioridade 1)

1 - ()

2 - ^

3 - \* e /

4 - + e -



Logo em seguida, serão realizadas as operações relacionais

Todos, sempre da esquerda para a direita>



Por fim, as operações lógicas

1 - E

2 - OU

3 - NAO





Estruturas condicionais:



1\) Condicionais Simples:



se (expressão) então

&#x20;  bloco

fimse





2\) Condicionais Compostas





Se (situação 1) então

&#x20;  Bloco A

senão

&#x20;  Bloco B

fimse



















3\) Estruturas (Condicionais) aninhadas SIMPLES



Se (situação 1) então

&#x20;  Bloco A

senão

&#x20;  Se (situação 2) então

&#x20;     Bloco B

&#x20;  senão

&#x20;     Bloco C

&#x20;  FimSe

FimSe





4\) Estrutura Condicional Escolha caso



escolha (variável)

&#x20; Caso (valor)

&#x20;  Bloco A

&#x20; Caso (valor)

&#x20;  Bloco B

&#x20; Caso (valor)

&#x20;  Bloco C

&#x20; Outro caso

&#x20;  Bloco D

FimEscolha





OBS's: para fazer condição em que tenha q ser um número entre um e outro utiliza-se



(var >= numero)  e  (var < numero)





Estruturas de Repetição 1:



Exemplo:

mao <- 0

Enquanto (mao <= 5) faça

&#x20;   troca

&#x20;   mao <- mao + 1

FimEnquanto





Sintaxe do comando ENQUANTO:



Enquanto (expressão) faca

&#x20;  bloco

FimEnquanto





Estruturas de Repetição 2:

Sintaxe:



Repita

&#x20;   Bloco

Ate expressão



(Repita um bloco ate que uma expressão ocorra)





Estrutura de Repetição 3 (Variável de controle):

Estrutura (Para):



Sintaxe:



Para **variável** <- **inicio** ate **fim** \[passo **salto]**  faca
*Bloco*
FimPara





**Rotinas:
Procedimentos:**


Procedimento NOME()
Inicio
  *//Conteúdo//*
FimProcedimento



**Passagem de Parâmetros (Procedimentos:**
*Tipo 1:* Por valor


Procedimento \*\*Soma(\*\*A, B: inteiro)
Inicio
  Escreval("Recebi o valor", A)
  Escreval("Recebi o valor", B)
  Escreval("A soma vale", A+B)
FimProcedimento

*Tipo 2: Por referência*

Procedimento **Soma**(var: A, B: inteiro)
inicio
  A <- A + 1
  B <- B + 2
  escreval("A soma vale", A+B)
fimprocedimento



**Escopo:
É o local onde uma determinada variável vai funcionar**

Rotinas 2

Funções:

Função Soma(A, B: inteiro) : inteiro
var
  S: inteiro
Inicio
  S <- A + B
  Retorne S
FimFuncao
Inicio
   N1 <- 5
   N2 <- 4
   RES <- Soma(N1,N2)
   Escreval("A soma é ", RES)
FimAlgoritmo

Passagem de Parâmetro (Funções)
Por valor e Por referência


Funções Prontas do VisuAlg
Valores Caractere

Site: caractere
Site <- "CursoEmVideo"

Compr(Site)
(Mostra o total de letras que tem no caractere)

Copia(Site, 6, 2)
(O primeiro numero indica a partir de qual letra começar a contar, e o segundo indica quantas letras mostrar após começar a contar)

Maiusc(Site)
(Mostra o caractere inteiro em letra Maiúscula)

Minusc(Site) 
(Mostra em letra Minúscula)

Pos("Video", Site)
(Mostra a posição da palavra indicada dentro da variável que você informou)

Asc("C") 
(Mostra o número da letra que vc informou)

Carac(67)
(Mostra a letra que esse numero representa)



VARIAVEIS COMPOSTAS PARTE 1:

ASSUNTO 1: VARIAVEIS COMPOSTAS HOMOGENEAS
(Compostas porque tem vários espaços dentro de uma variável. Homogêneas porque todos os espaços são do mesmo tipo.)

var
  n: vetor[1..4] de inteiro
inicio
  n[1] <- 3
  n[2] <- 5
  n[3] <- 1
  n[4] <- 0
fimalgoritmo

ASSUNTO 2: VARIAVEIS COMPOSTAS HOMOGENEAS UNIDIMENSIONAIS
(Compostas porque tem vários espaços dentro de uma variável. Homogêneas porque todos os espaços são do mesmo tipo.
Unidimensionais porque precisa apenas de um endereço para identificar cada um dos espaços.)

var
  n: vetor[1..4] de inteiro
  i: inteiro
inicio
  para i <- 1 ate 4 faca
     leia(n[i])
  fimpara
fimalgoritmo

ASSUNTO 3: ORDENAÇÃO DO VETOR

Se 1 valor menor que segundo valor
auxiliar recebe primeiro valor para guarda-lo
Primeiro valor recebe segundo valor
Segundo valor recebe Auxiliar





VARIAVEIS COMPOSTAS PARTE 1:

Variáveis Compostas Homogeneas Multidimensionais (Matrizes)

var
   m: vetor[1..3, 1..2] de inteiro















