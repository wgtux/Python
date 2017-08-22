#Leia uma palavra e troque as vogais por '*'.

p = input('Digite uma palavra: ')
i = 0
novapalavra = ''
while i < len(p):
    if p[i] in 'aeiou':
        novapalavra = novapalavra + '*'
    else:
        novapalavra = novapalavra + p[i]
    i += 1
print(novapalavra)
