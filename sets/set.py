meuSet = {1,2,3,4,1}
print(meuSet)

meuSet2 = set([1,2,3,4,7,8])
print(meuSet2)

meuSet.add(2)
print(meuSet)

meuSet.update([3,4,5,6])
print(meuSet)

meuSet.discard(2)
print(meuSet)

print(meuSet | meuSet2)
print(meuSet.union(meuSet2))

print(meuSet & meuSet2)
print(meuSet.intersection(meuSet2))

print(meuSet - meuSet2)
print(meuSet2.difference(meuSet))

print(meuSet^meuSet2)
print(meuSet.symmetric_difference(meuSet2))