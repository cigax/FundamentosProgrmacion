#La linea de codigo "with open("my_notes.txt", "w") as archivo:" crea un archivo llamado my_notes.txt
with open("my_notes.txt", "w") as archivo:
    #Las lineas archivo.write permiten introducir caracteres al documento
    archivo.write("Mis datos Personales\n")
    archivo.write("Hugo Fernandez\n")
    archivo.write("Estudiante\n")
    archivo.write("Ingenieria en las TIC\n")
#Imprime linea por linea el texto
with open("my_notes.txt", "r") as archivo:
    print(archivo.readline())
    print(archivo.readline())
    print(archivo.readline())
    print(archivo.readline())