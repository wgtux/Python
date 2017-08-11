'''
Leia um numero e diga se ele é IMPAR ou PAR.
'''
n = int(input('Digite um numero inteiro: '))
if n%2 ==0:
    print('O numero {} que você digitou é PAR!'.format(n))
else:
    print('O numero {} que você digitou é IMPAR!'.format(n))
