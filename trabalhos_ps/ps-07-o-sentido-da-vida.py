# Matheus Fernandes Melo
# 12121ECP017

def main():  # define a função main()
    fita = input().lower()  # recebe a string fita digitada e transforma suas letras em letras minusculas
    primer = input().upper()  # recebe a string primer digitada e transforma suas letras em letras maiusculas
    fita = fita.replace('5', '').replace('3', '')  # remove os números da string fita, pois eles não serão necessarios
    primer = inverte(primer).replace('5', '').replace('3', '')  # inverte a string atraves da função inverte() e
    # remove seus números
    primer = primer.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a')  # altera as bases do
    # primer (inicialmente em letras maiusculas) para as respectivas bases complementares(em letras minusculas)
    busca = buscar(fita, primer)  # recebe o resultado da função busca(), que verifica se o primer se liga na fita,
    # se sim tambem retorna as respectivas posições onde são ligadas
    if busca[0] == 0:  # caso não exista ligações:
        print('Nenhuma ligacao')  # imprime
    else:  # caso exista ligações:
        for i in range(len(busca[1])):  # cria um laço com o numero de ligações
            print(f'Ligacao na posicao {busca[1][i]}')  # imprime a posição da(s) ligação(ões)


def inverte(s):  # define a função inverte()
    ns = ''  # nova string inicialmente vazia
    for i in range(len(s)):  # cria um laço com o numero de caracteres da string recebi pela função
        ns += s[-(i + 1)]  # adiciona do ultimo ao primeiro item da antiga string ao final da nova string
    return ns  # retorna a nova string


def buscar(s, s1):  # define a função buscar() que recebe como parametros duas strings s e s1
    count = 0  # inicia uma variavel acumuladora
    pos = []  # cria uma lista pos(posição) vazia
    for i in range(len(s) - len(s1) + 1):  # cria um laço que fara o intervalo da diferença do número de caracteres
        # enter a primeira(s) e a segunda(s1) string mais 1
        if s1 == s[i:i + len(s1)]:  # verifica se existe a segunda string(s1) dentro do intervalo de caracteres que
            # esta sendo analisado na primeira string(s), se sim:
            count += 1  # soma mais 1 ao contador
            pos.append(i+1)  # adiciona a posição a lista pos
    return count, pos  # retorna o contador com o numero de ligações e uma lista com suas respectivas posições


main()  # chama a função main()
