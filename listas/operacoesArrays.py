from array import array

array_1 = array('B',[1,2,3,4,5,6])

array_1.insert(2,7)

array_1.remove(1)

for i in array_1:
    print(i)

print(30*'-')
print(array_1.index(4))

#print(array_1)

lista_simples_inteiro = [1, 2, 3, 8, 14, 4, 5]
lista_simples_inteiro.insert(0, 0)
lista_simples_inteiro.sort(reverse=True)
print(lista_simples_inteiro)