'''
Leia velocidade de um carro e se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por mk acima do limite
'''

v = int(input('Digite a Velocidade atual do Carro: '))
if v >80:
    multa = (v-80)*7
    print('Você ultrapassou a velocidade permitida de 80km/h')
    print('Sua velocidade foi de {}km/h e o valor da multa é de: R$ {}'.format(v,multa))
else:
    print('Parabens você não ultrapassou o limente de velocidade (80km/h)m sua velocidade foi de {}km/h'.format(v))
