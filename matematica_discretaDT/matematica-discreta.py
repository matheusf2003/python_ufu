def main():
    c1 = ['a']
    c2 = ['a', 'b']
    c3 = ['a', 'b', 'c']
    c4 = ['a', 'b', 'c', 'd']
    c5 = ['a', 'b', 'c', 'd', 'e']
    c20 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    saida_partes(c4)
    saida_prod(['a', 'b'], ['c', 'd'])


def partesde(c, tamanho_conjunto):  # c = conjunto
    tamanho_partes = 2 ** tamanho_conjunto
    partes = []
    for i in range(tamanho_partes):
        sc = []  # subconjunto
        for j in range(tamanho_conjunto):
            if (i & (2**j)) > 0:  # Utiliza o operador bitwise "&"
                sc.append(c[j])
        partes.append(sc)
    return partes


def produto_cart(c1, c2):
    produto = []
    for e1 in c1:
        for e2 in c2:
            produto.append([e1, e2])
    return produto


def saida_partes(c):
    print(f'Partes de: {c}')
    partes = partesde(c, len(c))
    print(partes)
    print(f'#P[c] = {len(partes)}')


def saida_prod(c1, c2):
    print(f'Produto {c1} x {c2}:')
    print(produto_cart(c1, c2))


if __name__ == "__main__":
    main()
