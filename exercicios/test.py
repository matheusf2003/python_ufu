def main():
    conjunto = ['a', 'b', 'c', 'd']
    print(partesde(conjunto, len(conjunto)))


def partesde(c, tamanho_conjunto):
    tamanho_partes = 2 ** tamanho_conjunto
    partes = []
    for counter in range(tamanho_partes):
        p = []
        for j in range(tamanho_conjunto):
            if (counter & (1 << j)) > 0:
                p.append(c[j])
        partes.append(p)
    return partes


if __name__ == "__main__":
    main()
