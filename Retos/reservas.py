import random

#Se busca en esta funcion obtener los datos personales de el usuario
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
#Se imprime las ciudades que estan incluidas 
def seleccionar_vuelo():
    print("\n--- Selección de Vuelo ---")
    ciudades = ["Medellín", "Bogotá", "Cartagena"]
    
    print("\nCiudades disponibles:")
    print("1. Medellín")
    print("2. Bogotá")
    print("3. Cartagena")
#Se solicita la ciudad de origen y se convierte la entrada a entero se resta el uno para ajustar a indices que comienzan en cero
# De la variable ciudades se asigna una ciudad y queda guardada en origen   
    origen_num = int(input("\nSeleccione número de ciudad de origen: "))
    origen = ciudades[origen_num - 1]
#Se solicita la ciudad de destino se convierte la entrada en entero y se resta el 1 para ajusta a indices que comienzan en cero   
#De la variable ciudad se asigna la ciudad de destino y queda guardada en destino
    destino_num = int(input("Seleccione número de ciudad de destino: "))
    destino = ciudades[destino_num - 1]
#Si la variable origen es igual a la de destino se debe imprimir el error y con el ciclo vuelve a preguntar un número diferente de destino
# Regresa con el cambio de la variable nueva   
    while origen == destino:
        print("Error: Origen y destino no pueden ser iguales.")
        destino_num = int(input("Seleccione número de ciudad de destino: "))
        destino = ciudades[destino_num - 1]
#Guarda en la variable dia_semana en minuscula   
    dia_semana = input("\nIngrese día de la semana (ej. lunes): ")
    dia_semana = dia_semana.lower()
#Guarda en la variable dia_mes el dia que va realizar el viaje, se agrega el ciclo para restringir los dias del 1 al 30 
# Si el usuario ingresa un numero menor a uno o mayor a 30 imprime el mensaje y vuelve a enviar el dia del mes para que guarde acorde a la restricción.    
    dia_mes = int(input("Ingrese día del mes (1-30): "))
    while dia_mes < 1 or dia_mes > 30:
        print("Día inválido. Debe ser entre 1 y 30.")
        dia_mes = int(input("Ingrese día del mes (1-30): "))
#Retorna o guarda todos los datos obtenidos por el usuario     
    return origen, destino, dia_semana, dia_mes
#Se tienen unos valores para el calculo del precio de acuerdo a su origen,destino y dia de la semana
def calcular_precio(origen, destino, dia_semana):
    distancias = {
        "Medellín-Bogotá": 240,
        "Bogotá-Medellín": 240,
        "Medellín-Cartagena": 461,
        "Cartagena-Medellín": 461,
        "Bogotá-Cartagena": 657,
        "Cartagena-Bogotá": 657
    }
    #Con los datos guardados obtenidos por el usuario se selecciona la opcion que tomo ejemplo: Si tomo la opción origen Medellin Destino Bogotá queda registrado en clave
    #Con la variable distancias se guarda la distancia que correspone de acuerdo a la variable clave
    clave = origen + "-" + destino
    distancia = distancias[clave]
 #El bucle sirve para determinar que dias si lleva el descuento
 # Si el es_dia_barato true solo cambia si hay coincidencia con la variable dia_semana   
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
#Asignacion de asiento
def asignar_asiento():
    print("\n--- Asignación de Asiento ---")
    print("Opciones de asiento:")
    print("1. Pasillo (Asiento C)")
    print("2. Ventana (Asiento A)")
    print("3. Sin preferencia (Asiento B)")
#El bucle condiciona para que el usuario solo tenga las tres opciones para la asignación de asiento   
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
#Imprime todos los datos calculados en el formato solicitado
def mostrar_resumen(nombre, origen, destino, dia_semana, dia_mes, precio, asiento, distancia):
    print("\n--- Resumen de Reserva ---")
    print("Pasajero: " + nombre)
    print("Vuelo: " + origen + " → " + destino)
    print("Fecha: " + dia_semana.capitalize() + " " + str(dia_mes) + " del mes")
    print("Distancia: " + str(distancia) + " km")
    print("Precio: $" + format(precio, ","))
    print("Asiento asignado: " + asiento)
    print("\n¡Gracias por elegir FastFast Airlines!")
#Funcion principal del código de las reservas
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
#Final de la estructura completa
if __name__ == "__main__":
    main()


