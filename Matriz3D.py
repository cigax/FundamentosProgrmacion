import random

# def define temperaturas alatorias
def temp_aleatoria():
    return random.randint(50, 100)
temperatura=[
    [#Ciudad de Quito
        [ #Semana
            {"day": "Lunes", "temp": random.randint(50, 100)},
            {"day": "Martes", "temp": random.randint(50, 100)},
            {"day": "Miércoles", "temp": random.randint(50, 100)},
            {"day": "Jueves", "temp": random.randint(50, 100)},
            {"day": "Viernes", "temp": random.randint(50, 100)},
            {"day": "Sábado", "temp": random.randint(50, 100)},
            {"day": "Domingo", "temp": random.randint(50, 100)}
        ]
    ],
    [#Ciudad de Cuenca
        [ #Semana
            {"day": "Lunes", "temp": random.randint(50, 100)},
            {"day": "Martes", "temp": random.randint(50, 100)},
            {"day": "Miércoles", "temp": random.randint(50, 100)},
            {"day": "Jueves", "temp": random.randint(50, 100)},
            {"day": "Viernes", "temp": random.randint(50, 100)},
            {"day": "Sábado", "temp": random.randint(50, 100)},
            {"day": "Domingo", "temp": random.randint(50, 100)}
        ]
    ],
    [ #Ciudad de Guayaquil
        [#Semana
            {"day": "Lunes", "temp": random.randint(50, 100)},
            {"day": "Martes", "temp": random.randint(50, 100)},
            {"day": "Miércoles", "temp": random.randint(50, 100)},
            {"day": "Jueves", "temp": random.randint(50, 100)},
            {"day": "Viernes", "temp": random.randint(50, 100)},
            {"day": "Sábado", "temp": random.randint(50, 100)},
            {"day": "Domingo", "temp": random.randint(50, 100)}
        ]
    ]
]
# Promedio de temperatura
ciudades = ["Quito", "Cuenca", "Guayakil"]
for ciudad_idx, ciudad in enumerate(temperatura):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")