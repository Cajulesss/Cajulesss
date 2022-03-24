#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:

#Perguntar qual a medida em metros a ser convertida:
perg = float(input("Digite a medida em metros para realizar a conversão em cm e mm:"))

#Adcionar as operações:
quil = perg/1000
hec = perg/100
deca = perg/10
cent = perg*100
dec = perg*10
mili = perg*1000

print("O valor da conversão para quilômetros é= {} km".format(quil))
print("O valor da conversão para hectômetros é= {} hm".format(hec))
print("O valor da conversão para decâmetros é= {} dam".format(deca))
print("O valor da conversão para centímetros é= {} cm".format(cent))
print("O valor da conversão para decímetros é = {} dm".format(dec))
print("O valor da conversão para milímetros é  ={}mm".format(mili,))