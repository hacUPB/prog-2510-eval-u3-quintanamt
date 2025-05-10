while True:
    # Mostrar el menú
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Pedir al usuario que elija una opción
    opcion = input("Elija una opción (1-5): ")

    # Salir del bucle si el usuario elige la opción 5
    if opcion == '5':
        print("Saliendo del programa...")
        break

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
    else:
        print("Opción no válida.")

 
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        print("Saliendo del programa...")
        break

while True:
    # Mostrar el menú
    print ("Menu: ")
    print("1. Pasta")
    print("2. Lasaña de Pollo")
    print("3. Pizza")
    print("4. Lasaña Vegetariana")
    print("5. Calzone")

    # Pedir al usuario que elija una opción
    plato = input("Elija una opción (1-5): ")


    # Descripción de los platos
    if opcion == '1':
        print("El plato", plato, "contiene Pasta libre de Gluten con una salsa Bechamel")
    elif opcion == '2':
        print("El plato", plato, "es una lasaña con pollo desmechado con una salsa de tomate, pan con ajonjolí")
    elif opcion == '3':
        print("El plato", plato, "es una pizza tamaño personal con Peperonni, jamón y salamí")
    elif opcion == '4':
        print("El plato", plato, "es una lasaña con base de grano, garbanzo, zanahoria, papá criolla con una salsa de tomates frescos con albahaca")
    elif opcion == '5':
        print("El plato", plato, "es una masa que sí contiene gluten con queso semidescremado y parmesano con carne y jamón dentro")
    else:
        print("Opción no válida.")

    # Preguntar si desea continuar
    continuar = input("¿Desea realizar otro plato a su pedido? (s/n): ")
    if continuar.lower() != 's':
        print("Saliendo del programa...")
        break