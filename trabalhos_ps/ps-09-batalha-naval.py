def main():
    lp = []  # listas de palpites
    t = [[i2 for i2 in input().split()] for i in range(10)]  # tabuleiro
    p = int(input())  # numero de palpites
    for i in range(p):
        lp.append(input().split())
    resultado = verifica(t, traduz(lp))
    for c in range(p):
        if resultado[0][c] == 0:
            print('agua')
        elif resultado[0][c] == 1:
            print(f'atingiu o navio {resultado[1][c]}')
        else:
            print(f'afundou o navio {resultado[1][c]}')


def verifica(t, coordenadas):
    ret = ([], [])  # uma tupla com duas listas, a primeira ira conter um numero para informar se o jogador
    # atingiu ou não um navio, sendo 0 = agua 1 = atingiu 2 = afundou, a segunda ira conter o navio que foi atingido
    navio = conta(t)
    for c in range(len(coordenadas[0])):
        item = t[coordenadas[0][c]][coordenadas[1][c]]
        if item != '.':
            ret[1].append(item)
            #navio.remove(item)
            encontra(navio, item, coordenadas, c)
            if item not in navio[0]:
                ret[0].append(2)
                apaga(item, t)
            else:
                ret[0].append(1)
        else:
            ret[0].append(0)
            ret[1].append(None)
    return ret


def conta(l):  # conta e identifica quantos navios possuem no tabuleiro
    navio = ([], [], [])
    for c1 in range(10):
        for c2 in range(10):
            if l[c1][c2] != '.':
                navio[0].append(l[c1][c2])
                navio[1].append(c1)
                navio[2].append(c2)
                #navio.append(c[c2])
    return navio


def encontra(navio, item, coordenada, c):
    for i in range(len(navio[0])):
        if navio[0][i] == item and navio[1][i] == coordenada[0][c] and navio[2][i] == coordenada[1][c]:
            for i2 in range(3):
                del(navio[i2][i])
            return navio


def apaga(item, t):
    for i in t:
        for i1 in range(10):
            if i[i1] == item:
                i[i1] = '.'
    return t


def traduz(lista):  # converte os palpites para numeros inteiros
    ll = []  # lista de linhas
    lc = []  # lista de colunas
    for p in lista:
        ll.append(ord(p[0].upper()) - 65)
        lc.append(int(p[1])-1)
    return ll, lc  # retorna duas listas de coordenadas sendo a primeira as linhas e a segunda as colunas


if __name__ == '__main__':
    main()
