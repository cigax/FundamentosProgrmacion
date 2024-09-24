#Diccionario con datos personales ficticios
informacion_personal={
    "nombres": "Antony ",
    "apellidos": "García Guevara",
    "edad": "23",
    "ciudad": "Cuenca",
}
#Imprime el diccionario original
print(informacion_personal)

#Nuevos datos agregados
informacion_personal ["ciudad"] = "Quito"
informacion_personal ["Profesión"] = "Arquitecto"
#Función if _ not in__ para agregar valor no encontrado
if "telefono" not in informacion_personal:
    informacion_personal["telefono"]="0987654321"
#Imprime el diccionario ahora con los nuevos datos
print(informacion_personal)


