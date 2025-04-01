
def mcd(num, den):
	if num <= den:
		menor = num
	else:
		menor = den
	for divisor in range(menor, 0, -1):
		if num % divisor == 0 and den % divisor == 0:
			max_com_div = divisor
			break
	return max_com_div

def imprime_fraccion(num, den,maximo):
	print (f"{num}\t \t{int (num/maximo)}")
	print ("______\t = \t______")
	print (f"{den}\t\t{int(den/maximo)}")