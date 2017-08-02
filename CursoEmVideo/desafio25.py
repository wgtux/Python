'''
Digite o nome e verifica se contem palavra SILVA
'''

nome = str(input('Digite o nome de uma Pessoa: ')).strip().lower()

t='silva' in nome

if t == True:
    print('O nome {} contém Silva'.format(nome))
else:
    print('O nome {}, nao contem SILVA'.format(nome))
