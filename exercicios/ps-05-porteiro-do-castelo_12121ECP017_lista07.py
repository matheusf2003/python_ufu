def main():
    senha = False
    lista = [int(i) for i in input().split()]
    lista_esperada = lista.copy()
    lista_esperada.sort()
    if lista_esperada == lista:
        senha = True
    else:
        for c in range(len(lista)-1):
            lista.insert(0, lista[-1])
            lista.pop()
            if lista_esperada == lista:
                senha = True
    if senha:
        print('Klift, Kloft, Still, a porta se abriu')
    else:
        print('Senha incorreta')


main()
