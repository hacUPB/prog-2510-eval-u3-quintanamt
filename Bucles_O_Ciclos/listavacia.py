import random

# Crear una lista vacía
lista_numeros = []

# Llenar la lista con 100 números aleatorios utilizando un bucle for
for i in range(100):
    numero_aleatorio = random.randint(1, 1000)  # Genera un número aleatorio entre 1 y 1000
    lista_numeros.append(numero_aleatorio)  # Agrega el número aleatorio a la lista

# Mostrar la lista resultante
print(lista_numeros)