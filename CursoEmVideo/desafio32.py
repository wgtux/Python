'''
Leia o ano e mostre se ele é bissexto
'''
a = int (input ('Digite ano para saber se é bissexto: '))

if a%4==0 or a%400==0 and a%100!=0:
    print('Ano {}, é Bissexto'.format(a))
else:
    print('O ano {}, não é Bissexto!'.format(a))
