numeroentero= int(input("Ingrese un número entero positivo: "))

print ("Tabla del" , numeroentero)
contador = 1
while contador <= 10:
    resultado = numeroentero * contador
    print(f"{numeroentero} x {contador} = {resultado}")
    contador += 1 

