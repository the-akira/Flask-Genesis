title: Gerando Números Aleatórios em Python
date: 2018-09-01
author: Gabriel Felippe
tags: [programming, python]

Neste artigo, vamos aprender como gerar números aleatórios em Python usando a biblioteca padrão `random`.

## Introdução

Gerar números aleatórios é uma tarefa comum em muitos programas e projetos de computação. Em Python, podemos facilmente gerar números aleatórios usando a biblioteca `random`.

## Implementação em Python

Aqui está um exemplo simples de como gerar números aleatórios em Python:

	:::python
	import random

	# Gerando um número aleatório inteiro entre 1 e 100
	numero_aleatorio = random.randint(1, 100)

	# Gerando um número aleatório de ponto flutuante entre 0 e 1
	numero_aleatorio_float = random.random()

	# Imprimindo os números aleatórios gerados
	print(f"Número aleatório inteiro: {numero_aleatorio}")
	print(f"Número aleatório de ponto flutuante: {numero_aleatorio_float}")