#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math

digite = float(input("Digite um número para realizar mostrar sua parte inteira:"))

arredondamento = math.floor(digite)

print("A parte inteira de {} é:{:.2f}".format(digite,arredondamento))