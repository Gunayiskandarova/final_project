lista = [56,34,47,78,99]
mx=max(lista[0],lista[1])
secondmx=min(lista[0],lista[1])
n = len(lista)
for i in range (2,n):
    if mx < lista[i]:
        secondmx=mx
        mx=lista[i]
print(secondmx)