# Detonando letreco e termo
    Código que resolve os jogos de palavra Letreco e Termo

[Vídeo demonstrativo de como jogar](https://youtu.be/2jWZJN17IqY)

## Objetivo
Asistindo as lives do [Casimiro](https://www.youtube.com/c/CortesdoCasimitoOFICIAL) jogando [Letreco](https://www.gabtoschi.com/letreco/) e [Termo](https://term.ooo/), pensei por que não fazer um código que resolve estes jogos. Deixo bem claro aqui que o objetivo não é trapacear, mas desenvolver lógica e conhecimentos de programação.

## Sobre os jogos
Os dois jogos são similares, todo dia eles lançam uma nova palavra que contém 5 letras e o objetivo do jogador é encontrar a palavra daquele dia em até 6 tentativas. Conforme o jogador vai arriscando qual é a palavra do dia, o sistema vai fornecer qual letra da palavra está na posição correta **(VERDE)** e qual está contida na palavra, mas não na posição certa **(AMARELO)** 

## Requirements
    python 3+

    pip install functools
    pip install Unidecode
    pip install regex
    python -m pip install -U matplotlib


    Or

    pip install -r requirements.txt

### Run
    python main.py

## Como usar o detonado

A interface é exatamente como demonstrado na imagem abaixo, para utilizar o app segue o passo a passo:

1. Clicar no botão **ENTER**
2. A palavra gerada aleatóriamente irá aparecer, digitar ela no Letreco ou termo
    1. Caso a palavra não seja encontrada, pode clicar no botão **TROCAR PALAVRA**
3. Depois de digitar a palavra no Letreco ou Termo e visualizar quais são as posições da palavra.
    1. Caso amarelo, de **1 clique** na letra para ela ficar em **AMARELO**, significando que está na palavra final, só não se sabe a posição.
    2. Caso verde, de **2 cliques** na letra para ela ficar em **VERDE**, significando que está na palavra final e nesta posição.
4. Após passar o gabarito para o app, seguir do passo 1 novamente até encontrar a palavra.

[Neste link](https://youtu.be/2jWZJN17IqY) tem um vídeo demonstrativo de como jogar

<figure>
    <img src="Image/Interface.PNG"
         alt="Interface"
         height="350">
    <figcaption>Uma demonstração da interface do app</figcaption>
</figure>

## Lógica

Na pasta Banco de palavras, há o arquivo original com todas as palavras da lingua portuguesa e o código utilizado para separar somente as que contém 5 letras e tratar elas: removendo repetições, deixando todas em minusculo e removendo caracteres especiais e acentos. Com isso temos 5428 palavras.

Com o banco de palavras formado a cada tentativa será fornecido uma palavra aleatória deste banco, retirando aquelas palavras via regex, que não tem chance nenhuma de ser a palavra do dia, desse modo, o banco de palavras inicial vai reduzindo até encontrar a palavra final.

As palavras podem ser retiradas seguindo alguns critérios:

- Todas as palavras que não contém as **letras verdes** nas suas repectivas posições
- Todas as palavras que contém as **letras amarelas** na posições que já é de conhencimento que não se encontram, e removendo palavras que não as contenham
- Remove todas as palavras que contém ao menos uma **letra cinza** da lista de bloqueio, que são aquelas que com certeza não estão na palavra final

## Resultados

O código contido em **termo_auto.py** testa a lógica de encontrar a palavra correta para n tentativas, abaixo se encontra os resultados destes testes:

| **n tentativas** 	| **% de acerto** 	| **Média de tentativas até acertar** 	|
|------------------	|:---------------:	|:-----------------------------------:	|
| 10               	|       100%      	|                 4,3                 	|
| 100              	|       95%       	|                 3,87                	|
| 1000             	|      95,1%      	|                 3,76                	|
| 10000            	|      95,6%      	|                 3,76                	|

