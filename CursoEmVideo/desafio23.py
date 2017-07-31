'''
Leia um numero de 0 a 9999 e mostre na tela cada um dos digitos seperados.
ex: num 1834
unidade:4
dezena:3
centena:8
milhar:1
'''

num = str(input('Digite um numero de 0 a 9999: '))
len(num) <4
print('Unidade',num[3])
print('Dezena',num[2])
print('Centena',num[1])
print('Milhar',num[0])