meuDicionario = {1:'William',2:'Paulo',3:'Maria',4:'Daniely'}
print(meuDicionario)

meuDicionario2 = dict({1:'William',2:'Paulo',3:'Maria',4:'Daniely'})
print(meuDicionario2)

for chave,valor in meuDicionario.items():
    print(f"A chave é {chave} e o valor {valor}")