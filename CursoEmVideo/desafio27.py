'''
Leia e nome de uma pessoa e mostre o primeiro e o ultimo nome dela
'''

p = str(input('Digite seu nome: ')).strip().lower()
d = p.split()
print('O seu primeiro nome é {}'.format(d[0]))
print('O seu Ultimo nome é {}'.format(d[len(d)-1]))
