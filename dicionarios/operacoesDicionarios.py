meuDicionario = {1: 'William', 2: 'Paulo', 3: 'Maria', 4: 'Daniely'}

print(meuDicionario[2])
print(meuDicionario.get(2))

print(len(meuDicionario))

meuDicionario.pop(2)
print(meuDicionario)

meuDicionario.clear()
print(meuDicionario)

meuDicionario[5] = 'Joaquina'
print(meuDicionario)
meuDicionario.update({6: 'Diego'})
print(meuDicionario)
