# EJercicio 
# 1. Solicitar al usuario una frase de al menos 30 palabras
# 2. Contar cuantas palabras hay en la frase 
# 3. Contar cuantos caracteres, incluyendo espacios en blanco hay en el texto
# 4. Contar los caracteres sin espacios en blanco
# 5. Contar cuantas veces se repite la vocal e y la vocal a 

# EJERCICIO: 


# Solicitar al usuario una frase de al menos 30 palabras
frase = input("Ingresa una frase con al menos 30 palabras: ")

# Contar cuantas palabras hay en la frase
cantidad_pal = len(frase.split())
print(cantidad_pal)

# Contar cuantos carácteres hay, incluyendo espacios en blanco hay en el texto
cantidad_caracteres = len(frase)
print(cantidad_caracteres)

# Contar los carácetres sin espacios

caracteres_sin_espacios = len(frase.replace(" ", ""))
print(caracteres_sin_espacios)

# Contar cuantas veces se repite la vocal a y la vocal e
letras_a = frase.lower().count("a")
letras_e = frase.lower().count("e")
print("Numero de letras a:",letras_a)
print("Numero de letras e:",letras_e)