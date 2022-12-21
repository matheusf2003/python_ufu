def main():
    li = int(input())
    matriz = [[i for i in input()] for i2 in range(li)]
    pos = [int(i) for i in input().split()]
    saida = [matriz[c][:] for c in range(len(matriz))]
    passou = [['' for c in range(len(matriz[0]))] for c2 in range(li)]
    fakenews(pos[1], pos[0], matriz, saida, passou)
    for c in range(li):
        for c2 in range(len(matriz[0])):
            print(f'{saida[c][c2]}', end='')
        if c < li:
            print()


def fakenews(x, y, matriz, saida, passou):
    if 0 <= x < len(matriz[0]) and 0 <= y < len(matriz):
        if matriz[y][x].isnumeric():
            if 'k' not in passou[y][x]:
                passou[y][x] += 'k'
                indice = int(matriz[y][x])
                if indice > 0:
                    direita(x, y, matriz, saida, indice, passou)
                    esquerda(x, y, matriz, saida, indice, passou)
                    cima(x, y, matriz, saida, indice, passou)
                    baixo(x, y, matriz, saida, indice, passou)
                saida[y][x] = 'X'


def direita(x, y, matriz, saida, indice, passou):
    if 'd' not in passou[y][x]:
        passou[y][x] += 'd'
        if matriz[y][x] != '#':
            if matriz[y][x].isnumeric():
                saida[y][x] = 'X'
                if int(matriz[y][x]) > 0 and x < len(matriz[0]):
                    fakenews(x, y, matriz, saida, passou)
    if indice > 0 and x < len(matriz[0])-1 and matriz[y][x] != '#':
        direita(x+1, y, matriz, saida, indice-1, passou)
    return saida


def esquerda(x, y, matriz, saida, indice, passou):
    if 'e' not in passou[y][x]:
        passou[y][x] += 'e'
        if matriz[y][x] != '#':
            if matriz[y][x].isnumeric():
                saida[y][x] = 'X'
                if int(matriz[y][x]) > 0 and x >= 0:
                    fakenews(x, y, matriz, saida, passou)
    if indice > 0 and x-1 >= 0 and matriz[y][x] != '#':
        esquerda(x-1, y, matriz, saida, indice-1, passou)
    return saida


def cima(x, y, matriz, saida, indice, passou):
    if 'c' not in passou[y][x]:
        passou[y][x] += 'c'
        if matriz[y][x] != '#':
            if matriz[y][x].isnumeric():
                saida[y][x] = 'X'
                if int(matriz[y][x]) > 0 and y >= 0:
                    fakenews(x, y, matriz, saida, passou)
    if indice > 0 and y - 1 >= 0 and matriz[y][x] != '#':
        cima(x, y-1, matriz, saida, indice-1, passou)
    return saida


def baixo(x, y, matriz, saida, indice, passou):
    if 'b' not in passou[y][x]:
        passou[y][x] += 'b'
        if matriz[y][x] != '#':
            if matriz[y][x].isnumeric():
                saida[y][x] = 'X'
                if int(matriz[y][x]) > 0 and y < len(matriz):
                    fakenews(x, y, matriz, saida, passou)
    if indice > 0 and y < len(matriz)-1 and matriz[y][x] != '#':
        baixo(x, y+1, matriz, saida, indice-1, passou)
        return saida


if __name__ == '__main__':
    main()
