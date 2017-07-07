#Determine se um ano é bissexto. Verifique no Google como fazer isso...

a = int (input ('Digite ano para saber se é bissexto: '))

if a%4==0 or a%400==0 and a%100!=0:
    print('Ano %6.0f, é Bissexto'%a)
else:
    print('O ano %6.0f, não é Bissexto!' %a)

