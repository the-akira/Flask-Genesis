title: Trabalhando com Strings em Python
date: 2018-01-01
author: Gabriel Felippe
tags: [programming, python]

Neste artigo, vamos explorar algumas operações básicas e úteis para manipulação de strings em Python.

## Introdução

Strings são sequências de caracteres em Python. Elas são amplamente utilizadas para representar texto e podem ser manipuladas de várias maneiras.

## Criando e Acessando Strings

Podemos criar strings simplesmente digitando o texto entre aspas simples ou duplas. Veja exemplos:

	:::python
	# Criando uma string
	mensagem = 'Olá, mundo!'

	# Acessando caracteres individuais da string
	primeiro_caractere = mensagem[0]
	ultimo_caractere = mensagem[-1]

	print("Primeiro caractere:", primeiro_caractere)
	print("Último caractere:", ultimo_caractere)