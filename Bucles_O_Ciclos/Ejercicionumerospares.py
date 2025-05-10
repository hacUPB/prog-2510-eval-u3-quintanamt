numeros_pares= int(input("Ingresa un número entero positivo: "))
numero = int(input("Cuantos pares quiere guardar? "))
numeros_pares = []

for i in range (numero):
  numeros_pares.append(2*(i+1))

print(f"La lista de los primeros {numero} números pares es {numeros_pares}")




