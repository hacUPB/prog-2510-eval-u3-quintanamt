# Mostrar el menú
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Módulo")

# Pedir al usuario que elija una opción
opcion = input("Elija una opción (1-5): ")

# Pedir dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if opcion == '1':
    print("Resultado:", num1 + num2)
elif opcion == '2':
    print("Resultado:", num1 - num2)
elif opcion == '3':
    print("Resultado:", num1 * num2)
elif opcion == '4':
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print("Resultado:", num1 / num2)
elif opcion == '5':
    print("Resultado:", num1 % num2)
else:
    print("Opción no válida.")