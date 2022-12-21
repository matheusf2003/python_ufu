def main():
    d1 = d1a = d2 = d2a = 0
    n = int(input())
    while n > 0:
        lote = int(input())
        n -= 1
        d1temp = vac(d1, d2, lote)[0]
        d2temp = vac(d1, d2, lote)[1]
        d1atemp = vacd1a(d1, d2, lote, d1a, d2a)[0]
        d2a = vacd1a(d1, d2, lote, d1a, d2a)[1]
        d1 = d1temp
        d2 = d2temp
        d1a = d1atemp

    # SAIDA
    print(f'Pessoas completamente imunizadas: {d2}\n'
          f'Pessoas imunizadas apenas com uma dose: {d1}\n'
          f'Pessoas que tomaram a segunda dose com atraso: {d2a}\n'
          f'Pessoas esperando a segunda dose com atraso: {d1a}')


def vac(d1, d2, lote):
    if d1 == 0:
        d1 = lote
    elif d1 >= lote:
        d1 -= lote
        d2 += lote
    elif d1 < lote:
        d2 += d1
        d1 = lote - d1
    return d1, d2


'''def vacd2(d1, d2, lote):
    if d1 == 0:
        d1 = lote
    elif d1 >= lote:
        d1 -= lote
        d2 += lote
    elif d1 < lote:
        d2 += d1
        d1 = lote - d1
    return d2'''


def vacd1a(d1, d2, lote, d1a, d2a):
    if d1 == 0:
        d1 = lote
    elif d1 >= lote:
        d1 -= lote
        if d1a != 0:
            d1a -= lote
            d2a += lote
        d1a = d1
        d2 += lote
    elif d1 < lote:
        d2 += d1
        d1 = lote - d1
        d2a += d1a
        d1a = 0

    return d1a, d2a


if __name__ == '__main__':
    main()
