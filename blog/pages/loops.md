title: Usando Loops em Python
date: 2018-01-01
author: Gabriel Felippe
tags: [programming, python]

Neste artigo, vamos aprender como usar loops em Python para executar instruções repetidamente e percorrer coleções de dados.

## Introdução aos Loops

Loops são estruturas de controle que nos permitem executar um bloco de código várias vezes. Em Python, temos duas principais formas de implementar loops: o loop `for` e o loop `while`.

## O Loop for

O loop `for` nos permite iterar sobre uma sequência de elementos, como uma lista, uma tupla, um dicionário ou uma string. Veja um exemplo:

    :::python
    # Iterando sobre uma lista de cores
    cores = ['vermelho', 'verde', 'azul']

    for cor in cores:
        print("Cor:", cor)