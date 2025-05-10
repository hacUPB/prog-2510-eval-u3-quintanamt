#Un elemento iterable es una estructura de datos 

# Crear una lista con su top 5 de canciones favoritas 
#Crear otra lista con el artista que la interpreta


# Listas de canciones favoritas y sus artistas
cancion_favorita = ["Igloo", "Love", "If you do", "English love affair", "La sin sentimientos"]
artista = ["KISS OF LIFE", "Keyshia Cole", "GOT7", "5 SECONDS OF SUMMER", "Alex Ponce"]

# Bucle WHILE: Recorre las listas usando un índice
indice = 0  # Empezamos desde el primer elemento
while indice < 5:  # Mientras el índice sea menor que 5 (hay 5 canciones)
    print(f"{cancion_favorita[indice]} La interpreta {artista[indice]}")  # Muestra canción + artista
    indice = indice + 1  # Pasamos al siguiente elemento

# Bucle FOR con RANGE: Recorre las listas usando un rango de números
for indice in range(5):  # Recorre los números del 0 al 4 (5 veces)
    print(f"{cancion_favorita[indice]} la interpreta {artista[indice]}")  # Muestra canción + artista

# Bucle FOR simple: Recorre solo la lista de canciones
for cancion in cancion_favorita:  # Recorre cada canción en la lista
    print(cancion)  # Muestra solo el nombre de la canción

#Agregar elementos a una lista
frutas = ["Manzana", "Banana", "Cereza"]

# Agregar un elemento al final de la lista
frutas.append("Damasco")

# Insertar un elemento en una posición específica
frutas.insert(5, "Fresa")

# Extender la lista con otra lista
frutas.extend(["Pera", "Kiwi, Mango"])

print(frutas)


# Eliminar Elementos de una lista
frutas = ["manzana", "banana", "naranja", "uva", "pera"]

# Eliminar un elemento por valor
frutas.remove("naranja")
print ("Frutas sin naranja", frutas)
# Eliminar un elemento por índice y obtener su valor
valor_eliminado = frutas.pop(1)
# Eliminar todos los elementos de la lista
frutas.clear()
print("Fruta Eliminada:", valor_eliminado)


nombres = ["Abigail", "Carla", "Evaligne", "Duvan"]

# Ordenar la lista alfabéticamente (ascendente)
nombres.sort()
print(nombres)
# Ordenar la lista alfabéticamente en orden descendente
nombres.sort(reverse=True)
print(nombres)
# Revertir el orden de la lista
nombres.reverse()
print(nombres)



BTS = ["KIM NAMJOON", "KIM SEOKJIN", "MIN JOONGI", "JUNG HOSEOK", "PARK JIMIN", "KIM THAEKJUN","KIM NAMJOON" , "JUNG JEONGUK"]

# Contar la cantidad de veces que aparece un elemento
CANTIDAD_BTS = BTS.count("KIM NAMJOON")

# Encontrar el índice de un elemento
indice_junghoseok = BTS.index("JUNG HOSEOK")

print("Cantidad de Kim Namjoon:", CANTIDAD_BTS)
print("Índice de Jung Hoseok:", indice_junghoseok)


texto = "hola, mundo!"
en_mayusculas = texto.upper()
print(en_mayusculas)  # Salida: "HOLA, MUNDO!"

texto = "Hola, Mundo!"
en_minusculas = texto.lower()
print(en_minusculas)  # Salida: "hola, mundo!"

texto = "hola, mundo!"
capitalizado = texto.capitalize()
print(capitalizado)  # Salida: "Hola, mundo!"

texto = "Python es genial"
reemplazado = texto.replace("genial", "increíble")
print(reemplazado)  # Salida: "Python es increíble"


frase = "Hola, cómo estás?"
palabras = frase.split(" ")
print(palabras)  # Salida: ['Hola,', 'cómo', 'estás?']

texto = "    Hola, mundo!   "
limpio = texto.strip()
print(limpio)  # Salida: "Hola, mundo!"

