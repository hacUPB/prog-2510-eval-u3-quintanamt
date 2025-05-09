
# Esta función solicita al usuario los datos necesarios para la simulación:
# la altitud inicial del satélite, el coeficiente de arrastre inicial y la altitud mínima segura.
# Devuelve estos tres valores como flotantes.
def solicitar_datos():
    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
    coef_arrastre = float(input("Introduzca el coeficiente de arrastre inicial: "))
    altitud_minima = float(input("Ingrese la altitud mínima segura (en kilómetros): "))
    return altitud_inicial, coef_arrastre, altitud_minima

# Esta función calcula la pérdida de altitud del satélite durante una órbita
# multiplicando la altitud actual por el coeficiente de arrastre.
# Devuelve la cantidad de altitud perdida.
def calcular_perdida_altitud(altitud_actual, coef_arrastre):
    return coef_arrastre * altitud_actual

# Esta función muestra en pantalla el estado del satélite en una órbita dada,
# incluyendo el número de órbita, la altitud actual y el coeficiente de arrastre,
# todos redondeados a cuatro cifras decimales para mayor claridad.
def mostrar_estado_orbita(orbita, altitud_actual, coef_arrastre):
    print("Órbita", orbita, ": Altitud actual =", round(altitud_actual, 4), "km, Coeficiente de arrastre =", round(coef_arrastre, 4))

# Esta función ejecuta la simulación del descenso del satélite.
# Utiliza un bucle para representar cada órbita, actualiza la altitud y el coeficiente de arrastre,
# y determina si el satélite ha reingresado a la atmósfera o si se ha estabilizado en una órbita baja.
def simular_desintegracion(altitud, coef_arrastre, altitud_minima):
    orbita = 0
    print("\nSimulando la desintegración orbital...")
    
    while True:
        orbita += 1
        altitud_perdida = calcular_perdida_altitud(altitud, coef_arrastre)
        altitud -= altitud_perdida
        coef_arrastre += 0.0001
        mostrar_estado_orbita(orbita, altitud, coef_arrastre)
        
        if altitud <= altitud_minima:
            print("\nEl satélite ha reingresado en la atmósfera terrestre después de", orbita, "órbitas.")
            break
        elif altitud_perdida < 0.01:
            print("\nEl satélite se ha estabilizado en una órbita baja.")
            print("Altitud final:", round(altitud, 4), "km")
            print("Órbitas completadas:", orbita)
            break

# Esta función principal coordina la ejecución del programa.
# Llama a la función para solicitar los datos y luego inicia la simulación.
def main():
    altitud, coef_arrastre, altitud_minima = solicitar_datos()
    simular_desintegracion(altitud, coef_arrastre, altitud_minima)


if __name__ == "__main__":
    main()



