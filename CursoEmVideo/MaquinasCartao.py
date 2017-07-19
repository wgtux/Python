# Desenvolver um sistema que simule as taxas de várias maquinas de cartão. Segue abaixo a tabela de algumas maquinas:

# 	       PayLeven	 Uol 1 dia	Paggnet	 Uol 30 dias
#debito	     2,49%	  2,39%	     2,30%	   2,39%
#credito	 4,19%	  5,59%	     4,30%	   3,79%
#cred. Parc. +2,49%	  2,99%	     1,90%	   2,99%

#Mostrar todas opções (debito, credito e parcelamento em até 10x) em todas maquininhas

debitoPay = 0.0249
creditoPay = 0.0419
creditoParcPay = 0.0249

debitoUol1 = 0.0239
creditoUol1 = 0.0559
creditoParcUol1 = 0.0299

debitoPagg = 0.0230
creditoPagg = 0.0430
creditoParcPagg = 0.0190

debitoUol30 = 0.0239
creditoUol30 = 0.0379
creditoParcUol30 = 0.0299


valor = float(input('Digite o Valor da Venda: '))
parcelacli = int(input('Digite a quantidade de parcela para simulação:'))
parcela = parcelacli-1

#Paylaven 02 Dias
debPl = -((valor*debitoPay)-valor)
crePl = -((valor*creditoPay)-valor)
creParcPl = -((((parcela*creditoParcPay)+(creditoPay))*valor)-valor)

#Uol 1dia
debUol = -((valor*debitoUol1)-valor)
creUol = -((valor*creditoUol1)-valor)
creParcUol = -((((parcela*creditoParcUol1)+(creditoUol1))*valor)-valor)

#Uol 30dias
debUol30 = -((valor*debitoUol30-valor))
creUol30 = -((valor*creditoUol30)-valor)
creParcUol30 = -((((parcela*creditoParcUol30)+(creditoUol30))*valor)-valor)

#Paggnet
debPg = -((valor*debitoPagg)-valor)
crePg = -((valor*creditoPagg)-valor)
creParcPg = -((((parcela*creditoParcPagg)+(creditoPagg))*valor)-valor)


print(10*'x','PAYLEVEN 02 DIAS',10*'x')
print('Debito PayLeven = ',debPl)
print('Credito PayLeven = ',crePl)
print('Credito Parcelado em %2.0i X = '%parcelacli, creParcPl)
print('A Empresa ficará com: R$',valor-creParcPl,'\n')

print(10*'x','UOL 1 DIA',10*'x')
print('Debito Uol 1 Dia = ',debUol)
print('Credito Uol 1 Dia = ',creUol)
print('Credito Parcelado em %2.0i X = '%parcelacli, creParcUol)
print('A Empresa ficará com: R$',valor-creParcUol,'\n')

print(10*'x','UOL 30 DIAS',10*'x')
print('Debito Uol 30 Dias = ',debUol30)
print('Credito Uol 30 Dias = ',creUol30)
print('Credito Parcelado em %2.0i X = '%parcelacli, creParcUol30)
print('A Empresa ficará com: R$',valor-creParcUol30,'\n')

print(10*'x','PAGGNET',10*'x')
print('Debito Paggnet = ',debPg)
print('Credito Paggnet = ',crePg)
print('Credito Parcelado em %2.0i X = '%parcelacli, creParcPg)
print('A Empresa ficará com: R$',valor-creParcPg,'\n')
