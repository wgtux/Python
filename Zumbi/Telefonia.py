#Considere uma empresa de telefona Tchau. Abaixo de 200 min, a empresa cobra R$ 0,20 por minuto.
#Entre 200 e 400 min, o preço é r$ 0,18. Acima de 400 min o preço por min é de R$ 0,15. Calcule sua conta de telefone.
#Promoção a 0,08 quando usar mais de 800 min

m = int(input("Quantos minutos foram foram usados?"))

if m < 200:
     tm = m*0.20
else:
     if m <= 400:
         tm = m * 0.18
     else:
         if m < 800:
             tm = m * 0.15
         else:
             tm = m * 0.08

print ('Conta Telefonica: R$%6.2f' %tm)

