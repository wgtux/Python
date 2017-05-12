#Aluguel de Carro

k = float(input('Quantos Km Percorridos:'))
d = float(input('Quantos Dias do Aluguel do Carro:'))
p=((d*60)+(0.15*k))
print ('O valor Total do Aluguel é de R$ %.2f' %p)
