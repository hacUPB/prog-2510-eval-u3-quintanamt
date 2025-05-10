
stroke = 50 

print("Bienvenido al sistema de inventario. Stock disponible:", stroke)

while stroke > 0: #Puse el while con 50 y era con Cero 
   
    entrada = int(input("¿Cuántos productos quieres comprar? ")) #La entrada era dentro del ciclo while y en el quiz lo puse afuera
    

    if entrada == 0: #No lo agregue en el código 
        print("Saliendo del sistema...")
        break #No lo agregue en el código 
    
  
    if entrada > stroke: #Puse el valor de stroke al inicial y no la variable como tal
        print("No hay suficientes productos disponibles.")
    else:
       
        stroke = stroke - entrada #Lo puse en el orden equivocado en el quiz
        print("Compra realizada. Stock restante:", stroke)
        

        if stroke == 0: #No puse esta parte 
            print("Inventario agotado.")