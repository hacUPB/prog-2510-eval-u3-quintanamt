

print("Tabla de Conversión Celsius a Fahrenheit")
print("------------------------------------------")
print("Celsius | Fahrenheit")
print("------- | ----------")
for celsius in range(0, 110, 10):
  fahrenheit = (celsius * 9/5) + 32
  print(f"{celsius:7} | {fahrenheit:10.2f}")