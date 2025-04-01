import random

def obtener_datos_usuario():
    print("\n--- Información del Usuario ---")
    titulo = input("Ingrese su título (Sr./Sra.): ")
    titulo = titulo.capitalize()
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.capitalize()
    apellido = input("Ingrese su apellido: ")
    apellido = apellido.capitalize()
    nombre_completo = titulo + " " + nombre + " " + apellido
    print("\n" + nombre_completo + ", ¡Bienvenido a FastFast Airlines!")
    return nombre_completo

def seleccionar_vuelo():
    print("\n--- Selección de Vuelo ---")
    ciudades = ["Medellín", "Bogotá", "Cartagena"]
    
    print("\nCiudades disponibles:")
    print("1. Medellín")
    print("2. Bogotá")
    print("3. Cartagena")
    
    origen_num = int(input("\nSeleccione número de ciudad de origen: "))
    origen = ciudades[origen_num - 1]
    
    destino_num = int(input("Seleccione número de ciudad de destino: "))
    destino = ciudades[destino_num - 1]
    
    while origen == destino:
        print("Error: Origen y destino no pueden ser iguales.")
        destino_num = int(input("Seleccione número de ciudad de destino: "))
        destino = ciudades[destino_num - 1]
    
    dia_semana = input("\nIngrese día de la semana (ej. lunes): ")
    dia_semana = dia_semana.lower()
    
    dia_mes = int(input("Ingrese día del mes (1-30): "))
    while dia_mes < 1 or dia_mes > 30:
        print("Día inválido. Debe ser entre 1 y 30.")
        dia_mes = int(input("Ingrese día del mes (1-30): "))
    
    return origen, destino, dia_semana, dia_mes

def calcular_precio(origen, destino, dia_semana):
    distancias = {
        "Medellín-Bogotá": 240,
        "Bogotá-Medellín": 240,
        "Medellín-Cartagena": 461,
        "Cartagena-Medellín": 461,
        "Bogotá-Cartagena": 657,
        "Cartagena-Bogotá": 657
    }
    
    clave = origen + "-" + destino
    distancia = distancias[clave]
    
    dias_baratos = ["lunes", "martes", "miércoles", "jueves"]
    es_dia_barato = False
    for dia in dias_baratos:
        if dia_semana == dia:
            es_dia_barato = True
            break
    
    if distancia < 400:
        if es_dia_barato:
            precio = 79900
        else:
            precio = 119900
    else:
        if es_dia_barato:
            precio = 156900
        else:
            precio = 213000
    
    return precio, distancia

def asignar_asiento():
    print("\n--- Asignación de Asiento ---")
    print("Opciones de asiento:")
    print("1. Pasillo (Asiento C)")
    print("2. Ventana (Asiento A)")
    print("3. Sin preferencia (Asiento B)")
    
    opcion = int(input("Seleccione su preferencia (1-3): "))
    while opcion < 1 or opcion > 3:
        opcion = int(input("Opción inválida. Seleccione 1-3: "))
    
    if opcion == 1:
        letra = "C"
    elif opcion == 2:
        letra = "A"
    else:
        letra = "B"
    
    numero = random.randint(1, 29)
    return str(numero) + letra

def mostrar_resumen(nombre, origen, destino, dia_semana, dia_mes, precio, asiento, distancia):
    print("\n--- Resumen de Reserva ---")
    print("Pasajero: " + nombre)
    print("Vuelo: " + origen + " → " + destino)
    print("Fecha: " + dia_semana.capitalize() + " " + str(dia_mes) + " del mes")
    print("Distancia: " + str(distancia) + " km")
    print("Precio: $" + format(precio, ","))
    print("Asiento asignado: " + asiento)
    print("\n¡Gracias por elegir FastFast Airlines!")

def main():
    print("=== Sistema de Reservas FastFast Airlines ===")
    
    # Paso 1: Información del usuario
    nombre_completo = obtener_datos_usuario()
    
    # Paso 2: Selección de vuelo
    origen, destino, dia_semana, dia_mes = seleccionar_vuelo()
    
    # Paso 3: Cálculo de precio
    precio, distancia = calcular_precio(origen, destino, dia_semana)
    
    # Paso 4: Asignación de asiento
    asiento = asignar_asiento()
    
    # Paso 5: Mostrar resumen
    mostrar_resumen(nombre_completo, origen, destino, dia_semana, dia_mes, precio, asiento, distancia)

if __name__ == "__main__":
    main()
    

