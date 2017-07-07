#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = int (input("Digite o primeiro valor"))
l2 = int (input("Digite o segundo valor"))
l3 = int (input("Digite o terceiro valor"))

#if (((l2 -l3)<l1<l2+l3) and ((l1-l3)<l2<l1+l3) and ((l1-l2)<l3<l1+l2)):
 #   print ('Esses valores podem formar um triangulo!')

    if l2==l1 and l2==l3:
        print('Triangulo Equilatero (3 lados iguais)!')
    else:
        if (l1!=l2 and l2!= l3 and l1!=l3):
            print('Triangulo Escaleno (3 lados diferentes)!')
        else:
            print("Triangulo Isosceles (dois lados iguais)!")
#else:
 #   print ('Não pode formar um triangulo!')