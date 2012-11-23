def g(n):
    if n == 0:
        return 1
    else:
        return n * g(n-1)

print (g(100))