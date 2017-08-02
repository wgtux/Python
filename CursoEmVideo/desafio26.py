'''
Faça o programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra "a"
Em que posição aparece a primeira vez
Em que posição ela aparece a ultima vez
'''

f = str(input('Digite uma Frase: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(f.count('a')))
print('A Primeira letra "A" aparece na posição {}'.format(f.find('a')))
print('A Ultima letra "A" aparece na posição {}')