def main():
	c = (1, 2, 3)
	print(c)
	pc = produto_cartesiano(c, c)
	print(pc)
	parte = partes(pc)
	#print(parte)
	for i in parte:
		clas = classifica(i, pc)
		print(f'{i} = {clas}')


def produto_cartesiano(c1, c2):
	return [(a, b) for a in c1 for b in c2]


def partes(c):
	resultado = [[]]
	for e in c:
		resultado += [sub+[e] for sub in resultado]
	return resultado


def classifica(rel, conj):
	s = ''
	s += reflexiva(rel, conj) + transitiva(rel, conj) + simetrica(rel, conj)
	if s == "RTS":
		s += 'E'
	return s


def reflexiva(rel, conj):
	for elem in conj:
		if not (elem, elem) in rel:
			return ''
	return 'R'


def transitiva(rel, conj):
	for a in conj:
		for b in conj:
			for c in conj:
				if (a, b) in rel and (b, c) in rel and not (a, c) in rel:
					return ''
	return 'T'


def simetrica(rel, conj):
	for a in conj:
		for b in conj:
			if (a, b) in rel and not (b, a) in rel:
				return ''
	return 'S'


'''def classifica(conj):
	for rel in partes in partes(produto_cartesiano(conj, conj))'''


if __name__ == "__main__":
	main()
