# Metodología del Sistema de Reservas de Aerolíneas (reservas.py)


**Pasos Principales:**

1.  **Bienvenida:** Se muestra un mensaje de bienvenida al usuario.

2.  **Información del Usuario:**
    * Se solicita al usuario que ingrese su título (Sr./Sra.), nombre y apellido mediante la función `input()`.
    * Se construye un saludo personalizado utilizando el nombre completo del usuario y se muestra en la consola con `print()`.

3.  **Selección de Vuelo:**
    * Se presentan las opciones de ciudades de origen (Medellín, Bogotá, Cartagena) al usuario mediante múltiples llamadas a `print()`.
    * Se solicita al usuario que ingrese el número correspondiente a su ciudad de origen usando `input()`.
    * Mediante una serie de estructuras condicionales `if/elif/else`, se asigna el nombre de la ciudad de origen a una variable. Se incluye una validación básica para opciones inválidas.
    * Se repite el proceso para la selección de la ciudad de destino.
    * Se verifica que la ciudad de origen y destino no sean la misma.

4.  **Fecha de Vuelo:**
    * Se solicita al usuario que ingrese el día de la semana y el día del mes deseado para el viaje, utilizando `input()`. El día del mes se convierte a entero con `int()`.

5.  **Cálculo del Precio del Billete:**
    * Se determina la distancia entre las ciudades seleccionadas mediante una serie de condicionales `if/elif`. Se asigna el valor de la distancia a una variable.
    * Se calcula el precio del billete basado en la distancia y el día de la semana, utilizando estructuras condicionales anidadas `if/elif/else`. Se evalúa si la distancia es menor o igual a 400 km y si el día de la semana es entre lunes y jueves o entre viernes y domingo. El precio resultante se asigna a una variable.

6.  **Asignación de Asiento:**
    * Se pregunta al usuario su preferencia de asiento (pasillo, ventana, sin preferencia) usando `input()`.
    * Se genera un número de asiento aleatorio entre 1 y 29 utilizando `random.randint(1, 29)`. Para esto, se importa el módulo `random` al inicio del script.
    * Se asigna una letra al asiento ('C' para pasillo, 'A' para ventana, 'B' para sin preferencia) mediante una estructura condicional `if/elif/else`.
    * Se combina el número y la letra del asiento en una sola cadena.

7.  **Salida:**
    * Se muestra un encabezado "--- Información de su Reserva ---" con `print()`.
    * Se muestra la información de la reserva: nombre completo, origen, destino, fecha de vuelo, precio del boleto (con formato de moneda colombiana) y asiento asignado, utilizando `print()` con cadenas f.

8.  **Mensaje Final:** Se muestra un mensaje de agradecimiento por usar el sistema.

**Características Clave de la Metodología:**

* **Lineal:** El programa se ejecuta de arriba hacia abajo, paso a paso.
* **Basado en Condicionales:** Se utilizan extensivamente las estructuras `if/elif/else` para la lógica de selección, cálculo de precios y asignación de asientos.
* **Entrada y Salida Directa:** Se utiliza `input()` para obtener información del usuario y `print()` para mostrar resultados.
* **Generación Aleatoria Simple:** Se emplea `random.randint()` para la asignación aleatoria del número de asiento.
* **Variables Claras:** Se utilizan variables con nombres descriptivos para almacenar la información del usuario, vuelo y reserva.
