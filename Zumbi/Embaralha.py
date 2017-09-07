'''
Defina uma função Embaralha que retorna as letras de uma String misturado.
'''

p = input('Digite uma palavra a ser embaralhada: ')

def embaralha(p):
    import random
    lista = list(p)
    random.shuffle(lista)
    return ''.join(lista)

print(embaralha(p))


