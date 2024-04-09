def invertir(palabra):
    p=""
    for l in palabra:
        p=l+p
    return p

t=input("ingresa algo -> ")
print(invertir(t))