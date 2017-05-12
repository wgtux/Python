#Total em segundos

d = int (input("Dias: "))
h = int (input("Horas: "))
m = int (input("Minutos: "))
s = int (input("Segundos: "))

t = (d*86400)
t = t +(h*3600)
t = t +(m*60)
t = t+s

print ("Total em Segundos: ",t)
