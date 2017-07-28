valor = float(input('Digite o Valor da Venda: '))
parcelacli = int(input('Digite a quantidade de parcela para simulação:'))
parcela = parcelacli - 1

taxaExcCielo = 0.05
anteCielo = 0.0397
mensCielo = 228
jurosTotal = 0
aluguelCielo = 114

# Cielo
count = 1
while count <= parcelacli:
    totalAntCielo = anteCielo * count
    parc = valor / parcelacli
    jurosPorParcela = (anteCielo * count)*parc
    jurosTotal = jurosPorParcela+jurosTotal

    print('Valor da Parcela de numero {c} é de R$ {p}'.format(c=count,p=parc))
    print('Valor do Juros é de R${j}'.format(j=jurosPorParcela),'\n')
    count += 1

totalGeral = jurosTotal+aluguelCielo
print('O valor Total da ANTECIPAÇÃO é de R$',jurosTotal)
print('ANTECIPAÇÃO + ALUGUEL DA UM TOTAL DE R$',totalGeral)
print('LUCRO NA VENDA PARCELADA COM ANTECIPAÇÃO R$', valor-jurosTotal)
print('Seu LUCRO no final do mês é de R$',valor-totalGeral)