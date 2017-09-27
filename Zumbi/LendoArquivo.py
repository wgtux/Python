#Lendo o arquivo que foi gerado anteriormente 'arquivo.py'

'''
arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
'''

#Jeito Python de Fazer
with open('numeros.txt') as f:
    print(f.read())