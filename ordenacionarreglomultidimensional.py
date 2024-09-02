matriz = [
    [3, 2, 1],
    [9, 7, 8],
    [6, 5, 4]
]

def ordenar_fila(matriz, fila):
    matriz[fila].sort()

fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
