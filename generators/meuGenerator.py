def elevaDois(max = 0):
    n = 0
    while n <= max:
        yield n*n
        n += 1

for i in elevaDois(5):
    print(i)  