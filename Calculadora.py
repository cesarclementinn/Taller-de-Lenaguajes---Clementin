# Función para aplicar descuento
def aplicar_descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)

# Función para aplicar IVA
def aplicar_iva(precio, porcentaje):
    return precio + (precio * porcentaje / 100)

# Función que procesa la cesta
def calcular_cesta(cesta, funcion):
    total = 0

    for producto, datos in cesta.items():
        precio = datos["precio"]
        porcentaje = datos["porcentaje"]

        total += funcion(precio, porcentaje)

    return total


# Ejemplo de cesta
cesta = {
    "Laptop": {"precio": 1000, "porcentaje": 10},
    "Mouse": {"precio": 50, "porcentaje": 5},
    "Teclado": {"precio": 80, "porcentaje": 21}
}

# Aplicar descuentos
total_descuento = calcular_cesta(cesta, aplicar_descuento)
print("Total con descuentos:", total_descuento)

# Aplicar IVA
total_iva = calcular_cesta(cesta, aplicar_iva)
print("Total con IVA:", total_iva)