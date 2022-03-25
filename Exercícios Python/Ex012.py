#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Seria 5% de (valor digitado pelo usuário)

#Vamos dizer que a pessoa queira comprar uma camiseta 
Prec = float(input("Digite o valor da camiseta escolhida:"))
desc = Prec*0.05
totdesc = Prec-desc

print("O desconto de 5% nessa camisa vale: {}R$".format(totdesc))