# Matheus Fernandes Melo
# 12121ECP017

f = a = e = w = 0  # Definição de variaveis == 0
# laço de repetição
while True:
    el = input().upper()  # entrada elemento
    if el == 'X':  # verifica se o laço de repetição deve ser quebrado
        break
    p = int(input())  # entrada pontuação
    if el == 'E':  # verifica se o elemento == Earth
        e += p  # soma o valor de "p" a variavel "e"
        a -= p / 2  # retira metade do valor de "p" do valor de "a"
    elif el == 'W':  # verifica se o elemento == Water
        w += p  # soma o valor de "p" a variavel "w"
        f -= p / 2  # retira metade do valor de "p" do valor de "f"
    elif el == 'F':  # verifica se o elemento == Fire
        f += p  # soma o valor de "p" a variavel "f"
        w -= p / 2  # retira metade do valor de "p" do valor de "w"
    elif el == 'A':  # verifica se o elemento == Air
        a += p  # soma o valor de "p" a variavel "a"
        e -= p / 2  # retira metade do valor de "p" do valor de "e"
    if e < 0:  # verifica se o valor de "e" é menor que 0 se verdadeiro iguala "e" a 0
        e = 0
    if w < 0:  # verifica se o valor de "w" é menor que 0 se verdadeiro iguala "w" a 0
        w = 0
    if f < 0:  # verifica se o valor de "f" é menor que 0 se verdadeiro iguala "f" a 0
        f = 0
    if a < 0:  # verifica se o valor de "a" é menor que 0 se verdadeiro iguala "a" a 0
        a = 0
# SAIDA
print('Pontuacao Final')
# imprime o valor final dos elementos
print(f'Agua: {w:.1f}\nTerra: {e:.1f}\nFogo: {f:.1f}\nAr: {a:.1f}')
if a > 0 and w > 0 and e > 0 and f > 0:  # verifica se todos elementos possuem valor maior que 0
    # se verdadeiro imprime este bloco
    print('Treinamento realizado com sucesso.')
else:
    # se falso imprime este bloco
    print('Realize mais treinamentos.')
