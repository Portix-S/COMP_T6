# COMP_T6

## Feito por:

- Gabriel Lourenço de Paula Graton - 800432
- Vitor Matheus da Silva - 800260
- Rafael Naoki Arakaki Uyeta - 800207
## Ferramentas

- Foi utilizado o Antlr 4.13
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

sinergia raze + fade
sinergia raze + breach
sinergia raze + deadlock
sinergia deadlock + geeko 
sinergia jett + skye
sinergia Jett + breach
sinergia jett + kayo
sinergia sage + raze
sinergia sova + phoenix
sinergia brimstone + cypher
sinergia breach + brimstone
sinergia breach + phoenix
sinergia cypher + killjoy
sinergia sage + sova
sinergia jett + omen


mapas bind raze + brimstone + skye + cypher + viper
mapas bind raze + brimstone + skye + killjoy + viper
mapas heaven jett + breach + fade + omem + killjoy
mapas lotus raze + fade + breach + chyfer omem

encontrar raze

// Saída esperada

sinergia com fade breach deadlock sage
composicao bind raze + brimstone + skye + cypher + viper
composicao bind raze + brimstone + skye + killjoy + viper
composicao lotus raze + fade + breach + chyfer omem

```

## Explicação Vídeo
A seguir há o vídeo explicado do trabalho.
