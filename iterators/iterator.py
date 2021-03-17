listaSimplesInteiro = [1,2,3,8,14,4,5]

meuIter = iter(listaSimplesInteiro)

# copiar do for
while True:
    try:
        elemento = next(meuIter)
        print(elemento)
    except StopIteration:
        break