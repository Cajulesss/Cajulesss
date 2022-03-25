"""Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área:"""

Lad1 = float(input("Digite a medida em metros da largura da parede:"))
Lad2 = float(input("Digite a medida em metros da altura da parede:"))

A = Lad1*Lad2
print("A área dessa parede é: {}m²".format(A))

"""E a quantidade de tinta necessária para pintá-la,sabendo que cada litro de tinta,pinta uma área de 2m²?"""
QT = 2
Tinta = A/2
print("A quantidade de tinta necessária para pintar toda essa área com tinta, seria:{}".format(Tinta))