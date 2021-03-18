set1 = {1,2}
set2 = {3,4}

setComprehensions = {i*i for i in range(0,10)}
print(setComprehensions)

setComprehensions2 = {i for i in set1.union(set2)}
print(setComprehensions2)