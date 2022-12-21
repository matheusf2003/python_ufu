def main():
    dmaior = int(input())  # dimensão do quadrado maior
    quadradomaior = criamatriz(dmaior)
    dmenor = int(input())  # dimensão do quadrado menor
    quadradomenor = criamatriz(dmenor)
    #print(f'{quadradomaior}\n\n{quadradomenor}')
    print((similaridade(quadradomaior, quadradomenor) / (len(quadradomenor) ** 2)) * 100)
    print('-=-=-=-=-')


def criamatriz(dimensão):
    matriz = []
    for i in range(dimensão):
        linha = input().split()
        matriz.append([])
        for i1 in linha:
            matriz[i].append(int(i1))
    return matriz


def similaridade(qmaior, qmenor):
    similar = 0
    maiorsimilar = 0
    for i in range(len(qmaior) - len(qmenor) + 1):
        for i2 in range(len(qmaior) - len(qmenor) + 1):
            print('++++++++++')
            if similar > maiorsimilar:
                maiorsimilar = similar
            similar = 0
            for i3 in range(len(qmenor)):
                for i4 in range(len(qmenor)):
                    print(f'p = qmaior[{i3}][{i2 + i4}]/ s = [{i3}][{i4}]')
                    if qmaior[i + i3][i2 + i4] == qmenor[i3][i4]:
                        similar += 1
    return maiorsimilar


main()
