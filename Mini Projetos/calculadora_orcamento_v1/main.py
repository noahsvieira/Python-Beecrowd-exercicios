'''

MINI PROJETO :  Calculadora de Orçamento

Cenário prático: imagine que um pequeno comércio precisa calcular o valor de uma compra com dois produtos.

O programa deverá:

1.Receber o nome de dois produtos.
2.Receber a quantidade de cada produto.
3.Receber o preço unitário.
4.Calcular o subtotal de cada produto.
5.Calcular o valor total.
6.Exibir um resumo da compra.

Esse projeto aproveita diretamente o aprendizado do exercício 1010, 
colocando os conhecimentos em uma situação prática.


2. O que precisamos usar para resolver?

Vamos reutilizar:

Conhecimento	        De onde veio

input()	                Beecrowd 1001 em diante
print()	                Beecrowd 1001 em diante
str	                    Entrada de nomes
int()	                Quantidade de produtos
float()	                Preço dos produtos
Multiplicação *	        Beecrowd 1004 e 1010
Soma +	                Beecrowd 1001 e 1003
f-string	            Beecrowd 1008, 1009 e 1010
:.2f	                Formatação monetária



# ENUNCIADO : 

Problema: Calculadora de Orçamento

Uma pequena loja precisa de um programa para calcular o valor de um pedido contendo dois produtos.

Você deverá desenvolver um programa que receba o nome, a quantidade e o preço unitário de cada produto.

O programa deverá calcular o subtotal de cada produto e, em seguida, apresentar o valor total do pedido.

Entrada

O programa deverá receber seis informações, nesta ordem:
1. Nome do primeiro produto.
2. Quantidade do primeiro produto.
3. Preço unitário do primeiro produto.
4. Nome do segundo produto.
5. Quantidade do segundo produto.
6. Preço unitário do segundo produto.


Saída

O programa deverá apresentar:
- Nome de cada produto e seu respectivo subtotal.
- Valor total do pedido.
- Valores monetários com duas casas decimais.

Exemplo de entrada
Teclado
2
50.00
Mouse
3
25.00


Exemplo de saída
--- RESUMO DO PEDIDO ---
Teclado: R$ 100.00
Mouse: R$ 75.00
-----------------------
TOTAL: R$ 175.00

'''

nome_produto_1 = int(input())
quantidade_1 = int(input())
preco_1 = float(input())

nome_produto_2 = int(input())
quantidade_2 = int(input())
preco_2 = float(input())

subtotal_1 = quantidade_1 * preco_1
subtotal_2 = quantidade_2 * preco_2

total = subtotal_1 + subtotal_2

print("\n ---RESUMO DO PEDIDO---")
print(f"{nome_produto_1}: R$ {subtotal_1:.2f}")
print(f"{nome_produto_2}: R$ {subtotal_2:.2f}")
print("----------------")
print(f"TOTAL: R$ {total:.2f}")