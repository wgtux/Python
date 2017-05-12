#Velocidade acima de 100km, aplicar multa de 5,00 por km ultrapassado

km = int(input("Qual a velocidade do carro:"))

if km > 100:
    m = ((km -100)*5)
    print("Sua Multa por ultrapassar a velocidade permitida é de R$ %5.2f " %m)
else:
    print("Sua velocidade estava abaixo de 100km/h")