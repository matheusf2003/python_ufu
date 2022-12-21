import time


def main():
	arquivo = open("arquivo5ele.txt", "w")
	c = (1, 2, 3, 4, 5)
	inicial = time.time()
	#arquivo.write(f'Conjunto: {c}\n')
	pc = produto_cartesiano(c)
	#arquivo.write(f'Produto cartesiano: {pc}\n')
	parte = partes(pc)
	#arquivo.write(f'Relações: {parte}\n')
	for i in parte:
		clas = classifica(i, pc)
		arquivo.write(f'{i} = {clas}\n')
	final = time.time()
	arquivo.write(f'Tempo total : {final - inicial}')




def produto_cartesiano(c1):
	return [(a, b) for a in c1 for b in c1]


def partes(c):
	resultado = [[]]
	for e in c:
		resultado += [sub+[e] for sub in resultado]
	return resultado


def classifica(rel, conj):
	s = ''
	s += reflexiva(rel, conj) + transitiva(rel) + simetrica(rel, conj)
	if s == "RTS":
		s += 'E'
	return s


def reflexiva(rel, conj):
	for elem in conj:
		if elem[0] == elem[1] and elem not in rel:
			return ''
	return 'R'


def transitiva(rel):
	for (a, b) in rel:
		for (c, d) in rel:
			if b == c and ((a, d) not in rel):
				return ''
	return 'T'


def simetrica(rel, conj):
	for a in conj:
		if a in rel and (a[1], a[0]) not in rel:
			return ''
	return 'S'





'''def classifica(conj):
	for rel in partes in partes(produto_cartesiano(conj, conj))'''



if __name__ == "__main__":
	main()
