#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

percorrido = float(input("Digite a quantidade de km percorridos:"))
dias = float(input("Digite a quantiade de dias que esse carro foi alugado:"))

dia = dias*60
km = percorrido*0.15
soma = dia + km
print("O valor a ser pago separado, por dia é: {} R$ e o valor a ser pago separado, por km rodados é: {:.2f}R$".format(dia,km))
print("Valor total a ser pago é: {:.2f} R$".format(soma))