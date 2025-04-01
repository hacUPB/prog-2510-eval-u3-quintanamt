def get_determinar_dia(numero_entero):
    if numero_entero == 1:
        dia = 'lunes'
    elif numero_entero == 2:
        dia = 'Martes'
    elif numero_entero == 3:
        dia = 'Miercoles'
    elif numero_entero == 4:
        dia = 'Jueves'
    elif numero_entero == 5:
        dia = 'Viernes'
    elif numero_entero == 6:
        dia = 'Sábado'
    elif numero_entero == 7:
        dia = "Domingo"
    return dia

def main():
    numero_entero = int(input("Ingrese un número del 1-7: "))

    if numero_entero <= 0 or numero_entero > 7:
        print("Número invalido")
    else: 
        dia = get_determinar_dia(numero_entero)
        print(f"El día es: {dia}")
    

if __name__ == "__main__": 
    main()