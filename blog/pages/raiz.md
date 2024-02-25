title: Calculando a Raiz Quadrada em Python
date: 2018-01-01
author: Gabriel Felippe
tags: [programming, python]

Neste artigo, vamos aprender como calcular a raiz quadrada de um número em Python. Python oferece uma maneira simples e direta de realizar essa operação usando a biblioteca padrão `math`.

## Introdução

Calcular a raiz quadrada de um número é uma operação comum em muitos programas e projetos matemáticos. No Python, podemos realizar essa operação facilmente usando a função `sqrt()` da biblioteca `math`.

## Implementação em Python

Aqui está um exemplo simples de como calcular a raiz quadrada de um número em Python:

	:::python
	import math

	# Definindo o número do qual queremos calcular a raiz quadrada
	numero = 25

	# Calculando a raiz quadrada usando a função sqrt() da biblioteca math
	raiz_quadrada = math.sqrt(numero)

	# Imprimindo o resultado
	print(f"A raiz quadrada de {numero} é {raiz_quadrada}")