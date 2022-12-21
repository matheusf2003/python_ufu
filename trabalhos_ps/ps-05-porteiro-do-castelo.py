# Matheus Fernandes Melo
# 12121ECP017

def main():  # define a função main()
    senha = False  # define a senha como errada por padrão
    lista = [int(i) for i in input().split()]  # entrada da lista
    lista_esperada = crescente(lista.copy())  # cria uma copia em ordem crescente da lista utilizando a função crescente() que ja foi definida no escopo global
    if lista_esperada == lista:  # verifica se a senha ja foi dada inicialmente na ordem correta
        senha = True  # define a senha como certa
    else:  # caso a senha não esteja inicialmente correta: faz a rotação e verificação da lista
        for c in range(len(lista) - 1):  # faz um loop que ira rodar c vezes sendo c = (numero de itens da lista)-1 pois a lista ja foi verificada uma vez
            lista.insert(0, lista[-1])  # coloca o ultimo item da lista na primeira posição
            lista.pop()  # exclui o ultimo item da lista
            if lista_esperada == lista:  # verifica se a lista esta em forma crescente, o programa ira verificar a cada rotação
                senha = True  # defina a senha com certa
    if senha:  # se a senha for certa
        print('Klift, Kloft, Still, a porta se abriu')  # mostra a mensagem que a porta se abriu
    else:  # se a senha fo errada
        print('Senha incorreta')  # mostra a mensagem que a porta esta fechada


def crescente(lista_antiga):  # define a função crescente
    nova_lista = []  # cria a nova lista inicialmente vazia
    for c in range(len(lista_antiga)):  # faz um loop que ira rodar c vezes sendo c = (numero de itens da lista)-1 pois a lista ja foi verificada uma vez
        m = menor(lista_antiga)  # m recebe o retorno da função menor()
        del(lista_antiga[m[1]])  # deleta o menor numero da lista
        nova_lista.append(m[0])  # adiciona o menor numero da lista_antiga a nova_lista
    return nova_lista  # retorna uma copia da lista em ordem crescente


def menor(lista):  # define a função menor()
    m = lista[0]  # m recebe o primeiro número da lista
    index = 0  # index recebe o valor 0 que equivale ao primeiro numero da lista
    for c in range(len(lista)):  # faz um loop que ira rodar c vezes sendo c = (numero de itens da lista)
        if m > lista[c]:  # se o valor armazenado em m(que inicialmente é o primeiro numero da lista) for menor que outro numero da lista
            m = lista[c]  # m recebe o novo menor numero da lista
            index = c  # index recebe o valor c que equivale a posição do novo menor numero da lista
    return m, index  # retorna o menor numero da lista e sua posição


main()  # chama a função main() para ser executada
