'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem formar um triangulo.
'''
l1 = int (input("Digite o primeiro valor: "))
l2 = int (input("Digite o segundo valor: "))
l3 = int (input("Digite o terceiro valor: "))

#if (((l2-l3)<l1<l2+l3) and ((l1-l3)<l2<l1+l3) and ((l1-l2)<l3<l1+l2)):
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
   print ('Esses valores podem formar um triangulo!')
else:
   print ('Não pode formar um triangulo!')