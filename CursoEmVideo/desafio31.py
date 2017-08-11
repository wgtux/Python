'''
Pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando 0,50 por km para viagens ate 200km
e 0,45 para viagens mais longas
'''
km = int(input('Qual a distancia da viagem em KM?'))
if km<=200:
    print('Sua Passagem fica no preço de R$ {}'.format(km*0.5))
else:
    print('Sua passagem ficou no preço de R$ {}'.format(km*0.45))
