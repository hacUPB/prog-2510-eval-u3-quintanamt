import random

print("¡Bienvenido al Sistema de Reservas de FastFast Airlines!")

# Información del usuario
titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_completo = titulo + " " + nombre + " " + apellido
print(f"{nombre_completo}, ¡Bienvenido a FastFast Airlines!")

# Selección de vuelo
print("\nSeleccione su origen:")
print("1. Medellín")
print("2. Bogotá")
print("3. Cartagena")
opcion_origen = input("Ingrese el número de su ciudad de origen: ")

if opcion_origen == '1':
    origen = "Medellín"
elif opcion_origen == '2':
    origen = "Bogotá"
elif opcion_origen == '3':
    origen = "Cartagena"
else:
    print("Opción de origen inválida.")
    exit()

print("\nSeleccione su destino:")
print("1. Medellín")
print("2. Bogotá")
print("3. Cartagena")
opcion_destino = input("Ingrese el número de su ciudad de destino: ")

if opcion_destino == '1':
    destino = "Medellín"
elif opcion_destino == '2':
    destino = "Bogotá"
elif opcion_destino == '3':
    destino = "Cartagena"
else:
    print("Opción de destino inválida.")
    exit()

if origen == destino:
    print("El origen y el destino no pueden ser iguales.")
    exit()

dia_semana = input("Ingrese el día de la semana en el que desea viajar (ejemplo: lunes): ").lower()
dia_mes = int(input("Ingrese el día del mes en el que desea viajar (un número entre 1 y 30): "))

# Cálculo del precio del billete
distancia = 0
if (origen == "Medellín" and destino == "Bogotá") or (origen == "Bogotá" and destino == "Medellín"):
    distancia = 240
elif (origen == "Medellín" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Medellín"):
    distancia = 461
elif (origen == "Bogotá" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Bogotá"):
    distancia = 657

precio = 0
if distancia < 400:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves":
        precio = 79900
    elif dia_semana == "viernes" or dia_semana == "sábado" or dia_semana == "domingo":
        precio = 119900
else:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves":
        precio = 156900
    elif dia_semana == "viernes" or dia_semana == "sábado" or dia_semana == "domingo":
        precio = 213000

# Asignación de asiento
preferencia_asiento = input("\n¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia?: ").lower()
numero_asiento = random.randint(1, 29)
letra_asiento = ""

if preferencia_asiento == "pasillo":
    letra_asiento = "C"
elif preferencia_asiento == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

asiento_asignado = str(numero_asiento) + letra_asiento

# Salida
print("\n--- Información de su Reserva ---")
print(f"Nombre completo: {nombre_completo}")
print(f"Origen: {origen}")
print(f"Destino: {destino}")
print(f"Fecha de vuelo: {dia_semana.capitalize()}, {dia_mes}")
print(f"Precio del boleto: ${precio:,.0f}".replace(",", "_TEMP_").replace(".", ",").replace("_TEMP_", "."))
print(f"Asiento asignado: {asiento_asignado}")

print("\n¡Gracias por reservar con FastFast Airlines!")
