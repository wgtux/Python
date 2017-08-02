'''
Digite o nome de uma cidade e verifica se começa ou não com a palavra SANTO
'''

c = str(input('Digite o nome de uma cidade: ')).strip().lower()

v = c.find('santo')

    if v == 0:
        print('A cidade {}, começa com a palavra SANTO'.format(c) )
    else:
        print('A cidade {}, não começa com a palavra SANTO!'.format(c))

#print(c.find('santo'))

