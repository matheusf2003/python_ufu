# Matheus Fernandes Melo
# 12121ECP017

#ENTRADA
s = int(input())
#ALGORITIMO
m = s // 60 #minutos totais
s %= 60 #resto de segundos
h = m // 60 #horas totais
m %= 60 #resto de minutos
d = h // 24 #dias
h %= 24 #resto de horas
#SAIDA
print(d, "dia(s),", h, "hora(s),", m, "minuto(s) e", s, "segundo(s).")
