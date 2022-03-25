"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar:"""
"""Considere:
US$ 1,00 = R$ 4,747
"""

Dinh = float(input("Digite o dinheiro em dólares para ser convertido em reais:"))

dolaremreal = 4.747
conver = (dolaremreal*Dinh)/1
print("A conversão em dólares desse valor é:{}R$".format(conver))
