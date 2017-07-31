'''
Leia nome completto de uma pessoa e mostre:
Nome com todas letras maisculas,
Quantas letras tem sem considerar espaços,
Quantas letras tem o 1 nome
e todas letras em minusculas
'''
nome = input('Digite seu nome completo: ')
n = nome.split()
print('Letras Maiusculas',nome.upper())
print('Letras Minúsculas',nome.lower())
print('Primeiro Nome tem : ',len(n[0]),'letras')
print('Seu nome tem ',len(nome.replace(' ','')) ,'Letras')

