# Matheus Fernandes Melo
# 12121ECP017

def main():  # define a função main()
    d1 = d1a = d2 = d2a = 0  # definição de variaveis
    n = int(input())  # entrada do número de meses que devem ser analisados pelo programa
    while n > 0:  # laço repetição
        lote = int(input())  # entrada de quantidade de vacinas disponiveis em cada mes
        n -= 1  # diminui a quantidade de meses que ainda serão adicionados
        tupla = vac(d1, d2, lote, d1a, d2a)  # variavel que recebe os valores que são retornados de função vac
        d1 = tupla[0]  # d1 recebe o primeiro dos valores retornados da função vac()
        d2 = tupla[1]  # d2 recebe o segundo dos valores retornados da função vac()
        d1a = tupla[2]  # d1a recebe o terceiro dos valores retornados da função vac()
        d2a = tupla[3]  # d2a recebe o quarto dos valores retornados da função vac()
    # SAIDA
    print(f'Pessoas completamente imunizadas: {d2}\n'  # imprime na tela o valor de d2
          f'Pessoas imunizadas apenas com uma dose: {d1}\n'  # imprime na tela o valor de d1
          f'Pessoas que tomaram a segunda dose com atraso: {d2a}\n'  # imprime na tela o valor de d2a
          f'Pessoas esperando a segunda dose com atraso: {d1a}')  # imprime na tela o valor de d1a


def vac(d1, d2, lote, d1a, d2a):  # função vac(): calcula os novos valores das variaveis d1, d2, d1a e d2a
    if d1 == 0:  # verifica se d1 é igual a 0. Se verdade:
        d1 = lote  # d1 recebe a quantidade de vacinas adicionadas naquele mes
    elif d1 >= lote:  # se d1 diferente de 0 e maior que a quantidade de vacinas adicionadas naquele mes:
        d1 -= lote  # d1 recebe o resultado da diferença entre d1 e a quantidade de vacinas
        if d1a != 0:  # se d1a é diferente de 0. Se verdade:
            d2a += lote  # d2a adiciona a seu valor a quantidade de vacinas naquele mes
        d1a = d1  # d1a recebe o valor d1
        d2 += lote  # d2 adiciona a seu valor a quantidade de vacinas naquele mes
    elif d1 < lote:  # se d1 menor que a quantidade de vacinas naquele mes:
        d2 += d1  # d2 adiciona a seu valor a quantidade de d1
        d1 = lote - d1  # d1 recebe o resultado da diferença entre a quantidade de vacinas naquele mes e d1
        d2a += d1a  # d2a adiciona a seu valor a quantidade de d1a
        d1a = 0  # d1 recebe 0
    return d1, d2, d1a, d2a  # retorna os novos valores das variaveis d1, d2, d1a, d2a


main()  # chama a função main(), para que o programa seja executado
