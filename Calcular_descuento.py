print("Gracias por comprar en LovelaceShop")
print("Por ser cliente frecuente de nuestra tienda podras recibir un descuento "
      "especial! Por favor ingresa el valor total de tu factura")

def calcular_descuento(valor_total, valor_descuento=15):
    descuento = valor_total * (valor_descuento / 100)
    return descuento
try:

    valor_total = float(input("Escribe el valor de tu prenda: "))
    descuento_compra = calcular_descuento(valor_total)
    valor_final = valor_total  - descuento_compra

    print(f"Gracias por tu compra, su monto total es  = ${valor_total}, tiene un descuento especial del 15% = ${descuento_compra:.2f}, el valor a pagar es = ${valor_final:.2f}")

except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido.")