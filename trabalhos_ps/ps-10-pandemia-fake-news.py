# Matheus Fernandes Melo
# 12121ECP017

def main():  # define a função main()
    li = int(input())  # recebe o numero de linhas da matriz
    matriz = [[i for i in input()] for i2 in range(li)]  # recebe a matriz
    pos = [int(i) for i in input().split()]  # recebe as posições para serem analizadas
    saida = [matriz[c][:] for c in range(len(matriz))]  # cria uma copia da matriz
    passou = [['' for c in range(len(matriz[0]))] for c2 in range(li)]  # cria uma matriz com as mesmas dimensões da
    # matriz original, ela sera usada para verificar se o item na coordenada ja foi analizado
    fakenews(pos[1], pos[0], matriz, saida, passou)  # chama a função que ira processar as informações fornecidas
    for c in range(li):  # cria um laço que ira percorrer as linhas da matriz
        for c2 in range(len(matriz[0])):  # cria um laço que ira percorrer as colunas da matriz
            print(f'{saida[c][c2]}', end='')  # imprime a saida da matriz
        if c < li:  # verifica se não é ultima linha da matriz
            print()  # pula uma linha


def fakenews(x, y, matriz, saida, passou):  # define a função fakenews()
    if 0 <= x < len(matriz[0]) and 0 <= y < len(matriz):  # verifica se as coordenadas informadas estão na matriz
        if matriz[y][x].isnumeric():  # verifica se o item analizado é um número
            if 'k' not in passou[y][x]:  # verifica se o item ja foi analizado anteriormente
                passou[y][x] += 'k'  # marca que o item foi analizado
                indice = int(matriz[y][x])  # adiciona a intensidade que a pessoa propaga fakenews a variavel indice
                if indice > 0:  # verifica se a intensidade de propagação é maior que 0
                    direita(x, y, matriz, saida, indice, passou)  # chama a função direita()
                    esquerda(x, y, matriz, saida, indice, passou)  # chama a função esquerda()
                    cima(x, y, matriz, saida, indice, passou)  # chama a função cima()
                    baixo(x, y, matriz, saida, indice, passou)  # chama a função baixo()
                saida[y][x] = 'X'  # substitui o item analizado por 'X'


def direita(x, y, matriz, saida, indice, passou):  # defina a função direita(), que infecta os individuos a direita
    if 'd' not in passou[y][x]:  # verifica se o item ja foi analizado anteriormente pela função
        passou[y][x] += 'd'  # marca que o item foi analizado
        if matriz[y][x] != '#':  # verifica se o item não é um bloqueio, caso seja ele não sera analizado
            if matriz[y][x].isnumeric():  # verifica se o item é um numero, caso não seja ele não sera alterado
                saida[y][x] = 'X'  # substitui o item analizado por 'X'
                if int(matriz[y][x]) > 0:  # verifica se a intensidade de propagação da pessoa analizada é maior que 0
                    fakenews(x, y, matriz, saida, passou)  # cama a função fakenews() para analizar a pessoa
    if indice > 0 and x < len(matriz[0])-1 and matriz[y][x] != '#':  # verifica se a intensidade de propagação ainda é
        # maior que 0 e se ainda existe(em) item(s) a direita, se sim:
        direita(x+1, y, matriz, saida, indice-1, passou)  # chama a função direita() para ser executada novamente,
        # diminuindo seu indice e indo um item a direita
    return saida  # retorna a matriz saida


def esquerda(x, y, matriz, saida, indice, passou):  # defina a função esquerda(), que infecta os individuos a esquerda
    if 'e' not in passou[y][x]:  # verifica se o item ja foi analizado anteriormente pela função
        passou[y][x] += 'e'  # marca que o item foi analizado
        if matriz[y][x] != '#':  # verifica se o item não é um bloqueio, caso seja ele não sera analizado
            if matriz[y][x].isnumeric():  # verifica se o item é um numero, caso não seja ele não sera alterado
                saida[y][x] = 'X'  # substitui o item analizado por 'X'
                if int(matriz[y][x]) > 0:  # verifica se a intensidade de propagação da pessoa analizada é maior que 0
                    fakenews(x, y, matriz, saida, passou)  # cama a função fakenews() para analizar a pessoa
    if indice > 0 and x-1 >= 0 and matriz[y][x] != '#':  # verifica se a intensidade de propagação ainda é
        # maior que 0 e se ainda existe(em) item(s) a esquerda, se sim:
        esquerda(x-1, y, matriz, saida, indice-1, passou)  # chama a função esquerda() para ser executada novamente,
        # diminuindo seu indice e indo um item a esquerda
    return saida  # retorna a matriz saida


def cima(x, y, matriz, saida, indice, passou):  # defina a função cima(), que infecta os individuos acima do item
    if 'c' not in passou[y][x]:  # verifica se o item ja foi analizado anteriormente pela função
        passou[y][x] += 'c'  # marca que o item foi analizado
        if matriz[y][x] != '#':  # verifica se o item não é um bloqueio, caso seja ele não sera analizado
            if matriz[y][x].isnumeric():  # verifica se o item é um numero, caso não seja ele não sera alterado
                saida[y][x] = 'X'  # substitui o item analizado por 'X'
                if int(matriz[y][x]) > 0:  # verifica se a intensidade de propagação da pessoa analizada é maior que 0
                    fakenews(x, y, matriz, saida, passou)  # cama a função fakenews() para analizar a pessoa
    if indice > 0 and y - 1 >= 0 and matriz[y][x] != '#':  # verifica se a intensidade de propagação ainda é
        # maior que 0 e se ainda existe(em) item(s) acima, se sim:
        cima(x, y-1, matriz, saida, indice-1, passou)  # chama a função cima() para ser executada novamente,
        # diminuindo seu indice e indo um item acima
    return saida  # retorna a matriz saida


def baixo(x, y, matriz, saida, indice, passou):  # defina a função baixo(), que infecta os individuos abaixo do item
    if 'b' not in passou[y][x]:  # verifica se o item ja foi analizado anteriormente pela função
        passou[y][x] += 'b'  # marca que o item foi analizado
        if matriz[y][x] != '#':  # verifica se o item não é um bloqueio, caso seja ele não sera analizado
            if matriz[y][x].isnumeric():  # verifica se o item é um numero, caso não seja ele não sera alterado
                saida[y][x] = 'X'  # substitui o item analizado por 'X'
                if int(matriz[y][x]) > 0:  # verifica se a intensidade de propagação da pessoa analizada é maior que 0
                    fakenews(x, y, matriz, saida, passou)  # cama a função fakenews() para analizar a pessoa
    if indice > 0 and y < len(matriz)-1 and matriz[y][x] != '#':  # verifica se a intensidade de propagação ainda é
        # maior que 0 e se ainda existe(em) item(s) abaixo, se sim:
        baixo(x, y+1, matriz, saida, indice-1, passou)  # chama a função baixo() para ser executada novamente,
        # diminuindo seu indice e indo um item abaixo
        return saida  # retorna a matriz saida


if __name__ == '__main__':  # verifica se o programa está sendo executado como um módulo ou script
    main()  # chama a função main() para ser executada
