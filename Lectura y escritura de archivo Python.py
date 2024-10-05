#La linea de codigo "with open("misdatos.txt", "w") as archivo:" crea un archivo llamado misdatos.txt
with open("misdatos.txt", "w") as archivo:
    #Las lineas archivo.write permiten introducir caracteres al documento
    archivo.write("Datos Personales\n")
    archivo.write("Hugo Fernandez\n")
    archivo.write("Estudiante\n")
    archivo.write("Ingenieria en las TIC\n")
#Imprime linea por linea el texto
with open("misdatos.txt", "r") as archivo:
    print(archivo.readline())
    print(archivo.readline())
    print(archivo.readline())
    print(archivo.readline())