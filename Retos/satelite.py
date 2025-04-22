import math

# Constantes físicas (aproximadas)
RADIO_TIERRA_KM = 6371
G = 6.67430e-11  # Constante de gravitación universal (m^3 kg^-1 s^-2)
MASA_TIERRA = 5.972e24  # Masa de la Tierra (kg)
ATMOSFERA_LIMITE_KM = 100  # Límite aproximado de la atmósfera terrestre

def obtener_datos_simulacion():
# Solicita al usuario los datos iniciales para la simulación."""
    while True:
        altitud_inicial_str = input("Ingrese la altitud inicial del satélite (en kilómetros): ")
        if altitud_inicial_str.replace('.', '', 1).isdigit():
            altitud_inicial = float(altitud_inicial_str)
            if altitud_inicial > 0:
                break
            else:
                print("La altitud inicial debe ser mayor que cero.")
        else:
            print("Error: Por favor, ingrese un valor numérico para la altitud.")

    while True:
        coeficiente_arrastre_str = input("Introduzca el coeficiente de arrastre inicial (ej. 0.001): ")
        if coeficiente_arrastre_str.replace('.', '', 1).isdigit():
            coeficiente_arrastre = float(coeficiente_arrastre_str)
            if coeficiente_arrastre >= 0:
                break
            else:
                print("El coeficiente de arrastre no puede ser negativo.")
        else:
            print("Error: Por favor, ingrese un valor numérico para el coeficiente de arrastre.")

    while True:
        altitud_minima_seguridad_str = input(f"Ingrese la altitud mínima segura (en kilómetros, menor que {ATMOSFERA_LIMITE_KM}): ")
        if altitud_minima_seguridad_str.replace('.', '', 1).isdigit():
            altitud_minima_seguridad = float(altitud_minima_seguridad_str)
            if 0 < altitud_minima_seguridad < ATMOSFERA_LIMITE_KM:
                break
            else:
                print(f"La altitud mínima segura debe estar entre 0 y {ATMOSFERA_LIMITE_KM} km.")
        else:
            print("Error: Por favor, ingrese un valor numérico para la altitud mínima segura.")

    return altitud_inicial, coeficiente_arrastre, altitud_minima_seguridad

def calcular_velocidad_orbital(altitud_km):
#Calcula la velocidad orbital circular a una altitud dada.
    radio_orbita = (altitud_km + RADIO_TIERRA_KM) * 1000  # Convertir a metros
    velocidad = math.sqrt(G * MASA_TIERRA / radio_orbita)
    return velocidad

def calcular_perdida_altitud(altitud_km, velocidad_ms, coeficiente_arrastre):
    """Calcula la pérdida de altitud por órbita debido al arrastre."""
    densidad_atmosferica = calcular_densidad_atmosferica(altitud_km)
#Simplificación: Asumimos una sección transversal y masa constantes para el satélite
#La pérdida de energía por arrastre es proporcional a la densidad, el cuadrado de la velocidad y el coeficiente de arrastre
    perdida_energia = 0.5 * densidad_atmosferica * (velocidad_ms ** 2) * coeficiente_arrastre
#Esta pérdida de energía se traduce en una pérdida de altitud (simplificación)
#Una simulación más precisa requeriría considerar la mecánica orbital detallada
    perdida_altitud_km = perdida_energia * 1e-6  # Factor de escala aproximado
    return max(0, perdida_altitud_km) # La pérdida no puede ser negativa

def calcular_densidad_atmosferica(altitud_km):
    """Estimación muy simplificada de la densidad atmosférica basada en la altitud."""
#Modelo exponencial simple (esto no es físicamente preciso, pero ilustra el concepto)
    escala_altura = 10  # km
    densidad_base = 1.225  # kg/m^3 (densidad al nivel del mar)
    if altitud_km > ATMOSFERA_LIMITE_KM:
        return 0.0
    return densidad_base * math.exp(-altitud_km / escala_altura)

def simular_orbita(altitud_km, coeficiente_arrastre):
    """Simula una órbita y calcula la nueva altitud."""
    velocidad_orbital = calcular_velocidad_orbital(altitud_km)
    perdida = calcular_perdida_altitud(altitud_km, velocidad_orbital, coeficiente_arrastre)
    nueva_altitud = max(0, altitud_km - perdida)
    nuevo_coeficiente_arrastre = coeficiente_arrastre * (1 + 0.01 * (1 - altitud_km / ATMOSFERA_LIMITE_KM)) # Aumenta al acercarse
    return nueva_altitud, nuevo_coeficiente_arrastre, perdida

def main():
    """Función principal para ejecutar la simulación de desintegración orbital."""
    print("=== Simulador de Desintegración Orbital de Satélite ===")
    altitud_inicial, coeficiente_arrastre_inicial, altitud_minima_seguridad = obtener_datos_simulacion()

    altitud_actual = altitud_inicial
    coeficiente_arrastre = coeficiente_arrastre_inicial
    orbita = 0

    print("\nSimulando la desintegración orbital...")

    while altitud_actual > altitud_minima_seguridad:
        orbita += 1
        nueva_altitud, nuevo_coeficiente_arrastre, perdida_altitud = simular_orbita(altitud_actual, coeficiente_arrastre)

        print(f"Órbita {orbita}: Altitud actual = {altitud_actual:.2f} km, Pérdida de altitud = {perdida_altitud:.4e} km, Coeficiente de arrastre = {coeficiente_arrastre:.4e}")

        if nueva_altitud >= altitud_actual and perdida_altitud < 1e-9: # Considerar estabilización
            print(f"\nEl satélite parece haberse estabilizado en órbita a una altitud de {altitud_actual:.2f} km después de {orbita} órbitas.")
            break

        altitud_actual = nueva_altitud
        coeficiente_arrastre = nuevo_coeficiente_arrastre

        if altitud_actual <= altitud_minima_seguridad:
            print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbita} órbitas.")
            break
        elif altitud_actual <= 0:
            print("\n¡El satélite ha impactado la superficie!")
            break

if __name__ == "__main__":
    main()