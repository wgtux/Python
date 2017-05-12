#Tempo de vida perdido do fumante

'''
   Fazendo uma regra de três chegamos que 144 cigarros tiram 1 dia
   de vida da pessoa (1 dia = 1440 minutos = 144 cigarros)
'''

c = int(input('Quantos Cigarros fuma por dia:'))
a = int(input('Quantos Anos já Fumou:'))
tc = a*360*c
v = tc/144
print('Você esta perdendo %.1f dias de vida'%v)
