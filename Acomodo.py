def SeleccionDirecta(lista):
    n = len(lista)
    print n
    print(“lista = “, lista[0])
    if n < 2:
        print(“Arreglo ordenado”)

    for i in range (0,  n - 1):
    
        pivote = lista[i]
 
        print(“pivote =“, pivote)
        for j in range (1, n - 1):
            if pivote > lista[j]:
                lista[i] = lista[j]
                lista[j] = pivote
                pivote = lista[i]

vector = [23,45,41,12,30,11]

print(“La lista ordenada es”, SeleccionDirecta(vector))
