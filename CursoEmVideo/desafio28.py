'''
Faça o computador pensar em um numero inteiro de 0 a 5 e o usuario tem que tentar adivinhar o numero
'''
from random import randint #importando o randint
from time import sleep #Importando o metodo Sleep que faz aguardar alguns segundos
r= randint(0,5)
print('-=-' *22)
print('Tente adivinhar o numero que estou pensando de 0 a 5')
print('-=-' *22)
n=int(input('Digite o numero:'))
print('PROCESSANDO...')
sleep(2)
if r == n:
        print('Você ACERTOU o numero {}...PARABÉNS!!!'.format(r))
else:
        print('Você ERROU o Computador sorteou o numero {} e Você digitou o numero {}'.format(r,n))
