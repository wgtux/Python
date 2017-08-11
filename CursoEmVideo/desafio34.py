'''
Salario de um funcionario e calcule o aumento. Salario superior a R$ 1.250,00 aumento de 10%
Inferior a esse valor 15%
'''
s = float(input('Digite o salario: R$'))
if s > 1250:
    nv = (s*0.10)+s
    print('Seu novo salrio com aumento de 10% é de R$ {}'.format(nv))
else:
    nv = (s*0.15)+s
    print('Seu novo salrio com aumento de 10% é de R$ {}'.format(nv))