# Desenvolver um sistema que simule as taxas de várias maquinas de cartão. Segue abaixo a tabela de algumas maquinas:

# 	       PayLeven	 Uol 1 dia	Paggnet	 Uol 30 dias
#debito	     2,49%	  2,39%	     2,30%	   2,39%
#credito	 4,19%	  5,59%	     4,30%	   3,79%
#cred. Parc. +1,99%	  2,99%	     1,90%	   2,99%

#Mostrar todas opções (debito, credito e parcelamento em até 10x) em todas maquininhas

valor = float(input('Digite o Valor da Venda: '))

#Paylaven
debPl = -((valor*0.0249)-valor)
crePl = -((valor*0.0419)-valor)
creParcPl = -((((9*0.0199)+(0.0419))*valor)-valor)

#Uol 1dia
debUol = -((valor*0.0239)-valor)
creUol = -((valor*0.0559)-valor)
creParcUol = -((((9*0.0299)+(0.0559))*valor)-valor)

#Uol 30dias
debUol30 = -((valor*0.0239)-valor)
creUol30 = -((valor*0.0379)-valor)
creParcUol30 = -((((9*0.0299)+(0.0379))*valor)-valor)

#Paggnet
debPg = -((valor*0.0230)-valor)
crePg = -((valor*0.0430)-valor)
creParcPg = -((((9*0.0190)+(0.0430))*valor)-valor)


print(10*'x','PAYLEVEN',10*'x')
print('Debito PayLeven = ',debPl)
print('Credito PayLeven = ',crePl)
print('Credito Parcelado em 10x = ',creParcPl,'\n')

print(10*'x','UOL 1 DIA',10*'x')
print('Debito Uol 1 Dia = ',debUol)
print('Credito Uol 1 Dia = ',creUol)
print('Credito Parcelado em 10x = ',creParcUol,'\n')

print(10*'x','UOL 30 DIAS',10*'x')
print('Debito Uol 30 Dias = ',debUol30)
print('Credito Uol 30 Dias = ',creUol30)
print('Credito Parcelado em 10x = ',creParcUol30,'\n')

print(10*'x','PAGGNET',10*'x')
print('Debito Paggnet = ',debPg)
print('Credito Paggnet = ',crePg)
print('Credito Parcelado em 10x = ',creParcPg,'\n')


