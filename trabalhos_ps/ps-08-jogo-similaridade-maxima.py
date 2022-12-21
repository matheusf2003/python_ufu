# Matheus Fernandes Melo
# 12121ECP017

def main():
    d = int(input())  # recebe a dimensão do quadrado maior
    m = [[int(n) for n in input().split()] for i in range(d)]  # recebe n linhas descrevendo o quadrado maior.
    d2 = int(input())  # recebe a dimensão do quadrado menor
    m2 = [[int(n) for n in input().split()] for i in range(d2)]  # recebe n linhas descrevendo o quadrado menor.
    maiorsimilar = encontraquadrado(m, m2, d2)  # recebe o retorno da função encontraquadrado()
    similaridade = maiorsimilar[0] / (d2 ** 2) * 100  # calcula a porcentagem de similaridade
    print(f'Posição: ({maiorsimilar[1][0]},{maiorsimilar[1][1]})\nSimilaridade máxima: {similaridade:.2f}%')  # imprime
    # na tela a saida contendo a posição e similaridade de maior grau de similaridade


def encontraquadrado(m, m2, d2):  # define a função encontramaior() que possui o objetivo de localizar o pedaço do
    # quadrado maior com maior grau di similaridade ao quadrado menor
    maximo = 0  # define a variavel maximo inicialmente com valor 0
    indicemx = [0, 0]  # cria a lista que contem o indice do quadrado a ser encontrado, inicialmente com [0, 0]
    for c0 in range(len(m) - d2 + 1):  # cria um laço que ira percorrer todas as linhas matriz do quadrado maior
        for c1 in range(len(m) - d2 + 1):  # cria um laço que ira percorrer todas as colunas matriz do quadrado maior
            indice = [c0, c1]  # guarda o indice do quadrado que esta sendo analisado
            nm = []  # cria uma nova matriz(nm) que ira receber o pedaço do quadrado maior maior, que esta
            # sendo analisado
            for c2 in range(d2):  # cria um laço que ira percorrer o pedaço da matriz m e inserir na nova matriz(nm)
                nm.append(m[c2 + c0][c1:c1 + d2])  # adiciona os novos valores a nova matriz(nm)
            pontossimilares = compara(m2, nm)  # recebe o retorno da função compara()
            if pontossimilares > maximo:  # se os pontos similares do pedaço que esta sendo analisado forem
                # maior do que o maximo, então:
                maximo = pontossimilares  # recebe a quantidade de pontos similares
                indicemx = indice  # recebe o indice do novo quadrado de maior similaridade
    return maximo, indicemx  # retorna o valor de maximo e o indice do mesmo


def compara(m2, nm):  # define a função compara()
    pontossimilares = 0  # cria a variavel pontossimilares inicialmente nula
    for c3 in range(len(m2)):  # cria um laço que ira percorrer todas as linhas matriz do quadrado menor
        for c4 in range(len(m2)):  # cria um laço que ira percorrer todas as linhas matriz do quadrado menor
            if m2[c3][c4] == nm[c3][c4]:  # verifica se os itens das matrizes são iguais, se sim:
                pontossimilares += 1  # adiciona + 1 a variavel pontossimilares
    return pontossimilares  # retorna a variavel pontossimilares


main()  # chama a função main() para ser executada
