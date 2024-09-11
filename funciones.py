#Importamos random para tener valores aleatorios
import random
#En este arreglo definimos las ciudades y las temperaturas aleatorias
temp_ciudad={
    "Quito": [random.randint(30,40) for _ in range(4)],
    "Cuenca": [random.randint(30,40) for _ in range(4)],
    "Guayaquil": [random.randint(30,40) for _ in range(4)],
    "Manta": [random.randint(30,40) for _ in range(4)]
}
# Función temperatura_ciudad para calcular las temperaturas aleatorias
def temperatura_ciudad (tem_ciudad):
#temperatura_promedio es un dicionario que almacena los datos promedios
    temperatura_promedio={}

    for ciudad,temperatura in temp_ciudad.items():
        promedio=sum(temperatura)/len(temperatura)
        temperatura_promedio[ciudad]=promedio
    #return devuelve el diccionario con los valores promedios
    return temperatura_promedio

promedios = temperatura_ciudad(temp_ciudad)

print("La temperatura promedio de la principales ciudadesd de Ecuador por un periodo de 4 semanas es: ")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")