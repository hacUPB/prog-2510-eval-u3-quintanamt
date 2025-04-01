
  


def get_puntuacion_letra(puntuacion):
    if puntuacion >= 90:
        return 'A'
    elif puntuacion >= 80:
        return 'B'
    elif puntuacion >= 70:
        return 'C'  
    elif puntuacion >= 60:
        return 'D'
    else:
        return 'F'

def main(): 
    try: 
        puntuacion = float(input("Ingrese su nota numérica (0-100): ")) 
        
        if puntuacion < 0 or puntuacion > 100:
            print("Error: La puntuación debe estar entre 0 y 100.")
            return 
         
        letra = get_puntuacion_letra(puntuacion) 
         

        print(f"Tu puntuación es: {letra}") 
    except ValueError:
        print("Por favor ingrese un número válido.") 
 
if __name__ == "__main__": 
    main()

