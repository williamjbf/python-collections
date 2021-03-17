listaSimplesInteiro = [1,2,3,8,14,4,5]
novaLista = []
for i in listaSimplesInteiro:
    novaLista.append(i*i)
print(novaLista)

novaListaElegante = [i*i for i in listaSimplesInteiro]
print(novaListaElegante)