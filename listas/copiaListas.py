import copy

nestedList = [[1,2,True],["Olá","Mundo"]]

# Deep Copy
novaLista = copy.deepcopy(nestedList)
nestedList[0][1] = 'A'
print(novaLista)
print(nestedList)

# Shallow Copy
outraLista = copy.copy(nestedList)
nestedList[0][1] = 'B'
print(outraLista)
print(nestedList)