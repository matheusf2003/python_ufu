# Matheus Fernandes Melo
# 12121ECP017

def main():  # define a função main()
    itens = int(input())  # numero de itens
    cap = int(input())  # capacidade da mochila
    peso = [int(input()) for i in range(itens)]  # entrada dos pesos
    valor = [int(input()) for i in range(itens)]  # entrada dos valores
    soma = ordenar(cap, peso, valor)  # define soma como os resultados da função ordenar()

    print(f'{soma[1]}\n{soma[0]}')  # imprime a saida do programa


def valp(peso, valor):  # define a função valp()
    valorpeso = []  # cria a lista que ira receber os valores das razões
    for c in range(len(peso)):  # cria um laço que ira rodar o numero de itens em peso
        valorpeso.append(valor[c] / peso[c])  # adiciona a lista o valor das razões
    return valorpeso  # retorna o valor da lista valorpeso


def ordenar(cap, peso, valor):  # define a função ordenar()
    soma_valor = 0  # cria a variavel soma_valor
    valorpeso = valp(peso, valor)  # cria a variavel que recebe a lista com tos das razões
    soma_peso = 0  # cria a variavel soma_peso
    while valor:  # cria o laço while que rodara enquanto a lista valor possuir itens
        bigger = maior(valorpeso)  # cria a variavel bigger que recebera o maior valor da lista valorpeso e seu index
        index_maior = bigger[1]  # cria uma variavel com o index do maior número
        contador = count(valorpeso, peso, bigger)  # cria uma variavel que recebe o retorno da função count()
        if contador[0]:  # verifica o primeiro item da variavel, que é um valor booleano
            index_maior = contador[1] + 1  # adiciona + 1 ao index que é retornado pela função count()
        if soma_peso + peso[index_maior] <= cap:  # se a soma do maior número da lista for menor ou igual a
            # capacidade da mochila:
            soma_peso += peso[index_maior]  # soma o peso a variavel soma_peso
            soma_valor += valor[index_maior]  # soma o valor a variavel soma_valor
            del(valor[index_maior])  # remove da lista o valor que foi utilizado
            del(peso[index_maior])  # remove da lista o peso que foi utilizado
            del(valorpeso[index_maior])  # remove da lista a razão que foi utilizada
        else:
            del(valor[index_maior])  # remove da lista o valor que não sera utilizado
            del(peso[index_maior])  # remove da lista o peso que não sera utilizado
            del(valorpeso[index_maior])  # remove da lista a razão que não sera utilizado
    return soma_peso, soma_valor  # retorna o resultado da função ordenar()


def count(valorpeso, peso, bigger):  # define a função count()
    copia = valorpeso.copy()  # cria uma copia da lista valorpeso
    copiap = peso.copy()  # cria uma copia da lista peso
    del(copiap[bigger[1]])  # remove o peso de maior razão da lista
    del(copia[bigger[1]])  # remove o peso de maior razão da lista
    if bigger[0] in copia:  # verifica se existe mais de um número com o maior razão na lista
        if peso[bigger[1]] > maior(copiap)[0]:  # verifica se o primeiro peso é maior
            bigger = maior(copiap)  # atualiza o maior numero da lista
            return True, bigger[1]  # retorna True e o novo maior número
    return False, None  # retorna False


def maior(lista):  # define a função maior()
    m = lista[0]  # m recebe o primeiro número da lista
    index = 0  # index recebe o valor 0 que equivale ao primeiro numero da lista
    for c in range(len(lista)):  # faz um loop que ira rodar c vezes sendo c = (numero de itens da lista)
        if m < lista[c]:  # se o valor armazenado em m(que inicialmente é o primeiro numero da lista) for maior que
            # outro numero da lista
            m = lista[c]  # m recebe o novo maior numero da lista
            index = c  # index recebe o valor c que equivale a posição do novo maior numero da lista
    return m, index  # retorna o maior numero da lista e sua posição


main()  # chama a função main() para ser executada
