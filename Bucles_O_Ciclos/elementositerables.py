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