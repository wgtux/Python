#Desconto
m = float(input("Qual o valor da mercadoria:"))
d = float(input("Qual a porcentagem de desconto:"))

vd = (m*d)/100
vt = m-vd
print ("Valor do desconto é de:",vd)
print("O valor total com desconto é de:",vt)
