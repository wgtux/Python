#Leia mensagem.txt e grave cripto.txt com todas as vogais trocadas por '*'

texto = open('mensagem.txt', 'w')
texto.write('Bem Vindo ao mundo Python')
texto.close()

msg = open('mensagem.txt', 'r')
saida = open('cripto.txt', 'w')
for linha in msg.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
msg.close()
saida.close()

with open('cripto.txt') as c:
    print(c.read())