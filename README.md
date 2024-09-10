# COMP_T6

## Feito por:

- Gabriel Lourenço de Paula Graton - 800432
- Vitor Matheus da Silva - 800260
- Rafael Naoki Arakaki Uyeta - 800207
## Ferramentas

- Foi utilizado o Antlr 4.7.2
- Foi utilizado o Python 3


## Trabalho

<p> Repositório feito em prol do desenvolvimento de um compilador para uma linguagem nova de Valorant.</p>
Valorant é um jogo de FPS da Riot Games, no qual é um embate de 5x5 em mapas, onde há uma parte de ataque e outra de defesa.
Em cada equipe é possível escolher agentes que podem ou não terem dois tipos de sinergia:

- Sinergia de Agentes - um agente consegue usar suas habilidades a fim de ajudar ( combar ) com outro.
- Sinergia de Mapas - um agente, em um mapa com outros 4, consegue trabalhar muito bem.

Com isso em mente, o nosso trabalho busca achar, dentre os agentes declarados, quais sinergias ele tem e em quais mapas também. Conforme o exemplo abaixo:
```
agente raze
agente fade
agente deadlock
agente breach
agente geeko
agente jett
agente skye
agente kayo
agente brimstone
agente cypher
agente sage
agente killjoy
agente viper
agente omem

sinergia sinergia1 raze fade
sinergia sinergia2 raze breach
sinergia sinergia3 raze deadlock
sinergia sinergia4 deadlock geeko 

mapa bind composicao raze + brimstone + skye + cypher + viper
mapa icebox composicao raze + brimstone + skye + killjoy + viper
mapa heaven composicao jett + breach + fade + omem + killjoy

encontrar sinergias para raze

// Saída esperada

raze possui sinergia com: fade; breach; deadlock; 
raze participa das seguintes composicoes: 
     bind: raze brimstone skye cypher viper 
     icebox: raze brimstone skye killjoy viper 

```

## Explicação Vídeo
A seguir há o vídeo explicado do trabalho.

https://github.com/user-attachments/assets/06f6a29c-08d1-4995-b02a-e1795b3016f3

