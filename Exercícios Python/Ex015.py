#Escreva um programa que converta uma temperatura digitada em °C para °F
# FÓRMULA: ((9*C)/5+32)

Fahrenheit = float(input("Digite a temperatura a ser convertida para graus Fahrenheit:"))
print("A converção de {} °C para °F é: {} °F".format(Fahrenheit,((9*Fahrenheit)/5+32)))