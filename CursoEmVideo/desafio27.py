'''
Leia e nome de uma pessoa e mostre o primeiro e o ultimo nome dela
'''

p = str(input('Digite seu nome: ')).strip().lower()
d = p.split()
print('O seu primeiro nome é: ',d[0])
print(d.count(d))
