# Desenvolver um sistema que simule as taxas de várias maquinas de cartão. Segue abaixo a tabela de algumas maquinas:

# 	       PayLeven	 Uol 1 dia	Paggnet	 Uol 30 dias
#debito	     2,49%	  2,39%	     2,30%	   2,39%
#credito	 4,19%	  5,59%	     4,30%	   3,79%
#cred. Parc. +2,49%	  2,99%	     1,90%	   2,99%

#Mostrar todas opções (debito, credito e parcelamento em até 10x) em todas maquininhas

valor = float(input('Digite o Valor da Venda: '))

debPl = -((valor*0.0249)-valor)
crePl = -((valor*0.0419)-valor)
print('Debito PayLeven = ',debPl)
print('Credito PayLeven = ',crePl)


