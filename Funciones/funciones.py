import fraccion

# función principal
def main():
	numerador = int(input("Ingrese el numerador:"))
	denominador = int(input("Ingrese el denominador:"))
	maximo = fraccion.mcd(numerador, denominador)
	print(f"M.C.D = {maximo}")
	fraccion.imprime_fraccion(numerador,denominador, maximo)
# Punto de entrada del programa
if __name__ == "__main__":
	main()
	