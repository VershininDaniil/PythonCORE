def nod(x, y):
    if y == 0:
        return x
    else:
        return nod(y, x % y)
    

a, b = map(int, input().split())

print(nod(a, b))