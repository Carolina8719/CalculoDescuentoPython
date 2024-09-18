def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con monto total
    monto1 = 1000  # Ejemplo de monto total
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento: ${descuento1:.2f} (10%)")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 500  # Ejemplo de monto total
    porcentaje2 = 20  # Ejemplo de porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento: ${descuento2:.2f} ({porcentaje2}%)")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

