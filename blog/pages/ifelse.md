title: Usando Condicionais em Python
date: 2018-01-01
author: Gabriel Felippe
tags: [programming, python]

Neste artigo, vamos aprender como usar condicionais em Python para controlar o fluxo do nosso programa com base em diferentes condições.

## Introdução

As condicionais em Python nos permitem executar blocos de código com base em condições específicas. Podemos usar as estruturas `if`, `elif` e `else` para controlar o fluxo do programa de acordo com as condições definidas.

## Usando a Estrutura If

A estrutura `if` nos permite executar um bloco de código se uma condição for avaliada como verdadeira. Veja um exemplo:

    :::python
    # Verificando se um número é positivo, negativo ou zero
    numero = 10

    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")