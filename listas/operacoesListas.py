listaSimplesInteiro = [1, 2, 3, 8, 14, 4, 5]
listaSimplesString = ["Olá", "Mundo"]
listaSimplesMesclada = [1, 2, 3, "Olá, mundo", True, 1.5]
nestedList = [[1, 2, True], ["Olá", "mundo"]]

print(listaSimplesInteiro)
print(nestedList)

# Len()
print(len(listaSimplesMesclada))
print(len(nestedList))

# Append()
listaSimplesInteiro.append(6)
print(listaSimplesInteiro)

# Insert()
listaSimplesInteiro.insert(2, "Olá")
print(listaSimplesInteiro)

# Remove()
listaSimplesInteiro.remove(1)
print(listaSimplesInteiro)

# Index()
index = listaSimplesInteiro.index(3)
print(index)

# Count()
count = listaSimplesInteiro.count(3)
print(count)

# Sort()
lista_string = ["A", "B", "C"]
lista_string.sort(reverse=True)
print(lista_string)