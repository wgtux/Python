'''
Leia o ano e mostre se ele é bissexto
'''

from datetime import date #importando biblioteca para pegar ano atual

a = int(input('Digite ano para saber se é bissexto ou 0 para ver o ano atual '))
if a == 0:
    a = date.today().year #pegando o ano atual
if a%4==0 and a%100!=0 or a%400==0 :
    print('Ano {}, é BISSEXTO!'.format(a))
else:
    print('O ano {}, não é BISSEXTO!'.format(a))
