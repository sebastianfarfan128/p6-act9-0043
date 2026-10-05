# Sebastian Farfan NC = 0043
# EJERCICIOS DE PYTHON: VARIABLES, TIPOS DE DATOS Y OPERADORES
# Basado en la documentación de W3Schools

# 1. Variables en Python 0043 (python_variables.asp)

# Ejemplo 1: Creación y asignación básica de variables
nombre_persona = "Ana"
edad = 25
altura_metros = 1.68

print("--- 1. Variables - Ejemplo 1 ---")
print("Nombre:", nombre_persona)
print("Edad:", edad)
print("Altura:", altura_metros)

# Ejemplo 2: Reasignación y cambio de tipo dinámico
x = 10          # x es de tipo int
x = "Python"    # x ahora es de tipo str

print("\n--- 1. Variables - Ejemplo 2 ---")
print("Valor actual de x:", x)

# Ejemplo 3: Conversión explícita de tipos (Casting)
numero_cadena = str(3)     # '3'
numero_entero = int(3)     # 3
numero_flotante = float(3) # 3.0

print("\n--- 1. Variables - Ejemplo 3 ---")
print("Casting str():", numero_cadena, "| Tipo:", type(numero_cadena))
print("Casting int():", numero_entero, "| Tipo:", type(numero_entero))
print("Casting float():", numero_flotante, "| Tipo:", type(numero_flotante))


# 2. Asignación Múltiple de Variables 0043 (python_variables_multiple.asp)

# Ejemplo 1: Múltiples valores a múltiples variables
fruta1, fruta2, fruta3 = "Manzana", "Banana", "Cereza"

print("\n--- 2. Variables Múltiples - Ejemplo 1 ---")
print("Fruta 1:", fruta1)
print("Fruta 2:", fruta2)
print("Fruta 3:", fruta3)

# Ejemplo 2: Un mismo valor asignado a múltiples variables
x = y = z = "Naranja"

print("\n--- 2. Variables Múltiples - Ejemplo 2 ---")
print("x:", x, "| y:", y, "| z:", z)

# Ejemplo 3: Desempaquetado de una colección (Unpacking)
colores = ["Rojo", "Verde", "Azul"]
c1, c2, c3 = colores

print("\n--- 2. Variables Múltiples - Ejemplo 3 ---")
print("Color 1:", c1)
print("Color 2:", c2)
print("Color 3:", c3)


# 3. Tipos de Datos 0043 (python_datatypes.asp)

# Ejemplo 1: Tipos numéricos y texto (int, float, str)
texto = "Hola, Mundo!"
entero = 42
decimal = 3.1416

print("\n--- 3. Tipos de Datos - Ejemplo 1 ---")
print(f"'{texto}' es de tipo:", type(texto))
print(f"{entero} es de tipo:", type(entero))
print(f"{decimal} es de tipo:", type(decimal))

# Ejemplo 2: Colecciones (list, tuple, dict, set)
lista_frutas = ["manzana", "banana"]
tupla_coordenadas = (10, 20)
diccionario_usuario = {"nombre": "Carlos", "edad": 30}
conjunto_numeros = {1, 2, 3}

print("\n--- 3. Tipos de Datos - Ejemplo 2 ---")
print("Lista:", lista_frutas, "->", type(lista_frutas))
print("Tupla:", tupla_coordenadas, "->", type(tupla_coordenadas))
print("Diccionario:", diccionario_usuario, "->", type(diccionario_usuario))
print("Set:", conjunto_numeros, "->", type(conjunto_numeros))

# Ejemplo 3: Booleans y None (bool, NoneType)
es_activo = True
valor_nulo = None

print("\n--- 3. Tipos de Datos - Ejemplo 3 ---")
print("es_activo:", es_activo, "->", type(es_activo))
print("valor_nulo:", valor_nulo, "->", type(valor_nulo))


# 4. Operadores Aritméticos 0043 (python_operators_arithmetic.asp)

# Ejemplo 1: Suma (+), Resta (-), Multiplicación (*)
a = 15
b = 4

print("\n--- 4. Operadores Aritméticos - Ejemplo 1 ---")
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)

# Ejemplo 2: División (/), División entera (//), Módulo (%)
print("\n--- 4. Operadores Aritméticos - Ejemplo 2 ---")
print(f"{a} / {b} =", a / b)   # Resultado flotante
print(f"{a} // {b} =", a // b) # Resultado entero (descarta residuo)
print(f"{a} % {b} =", a % b)   # Residuo de la división

# Ejemplo 3: Potencia (**) y operaciones combinadas con jerarquía
base = 2
exponente = 3
resultado_complejo = (5 + 3) * 2 ** 2

print("\n--- 4. Operadores Aritméticos - Ejemplo 3 ---")
print(f"{base} ** {exponente} =", base ** exponente)
print("Resultado de (5 + 3) * 2 ** 2 =", resultado_complejo)


# 5. Operadores de Comparación 0043 (python_operators_comparison.asp)

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
num1 = 20
num2 = 20
num3 = 30

print("\n--- 5. Operadores de Comparación - Ejemplo 1 ---")
print(f"{num1} == {num2}:", num1 == num2)
print(f"{num1} != {num3}:", num1 != num3)

# Ejemplo 2: Mayor que (>), Menor que (<)
print("\n--- 5. Operadores de Comparación - Ejemplo 2 ---")
print(f"{num3} > {num1}:", num3 > num1)
print(f"{num1} < {num3}:", num1 < num3)

# Ejemplo 3: Mayor o igual (>=), Menor o igual (<=)
print("\n--- 5. Operadores de Comparación - Ejemplo 3 ---")
print(f"{num1} >= {num2}:", num1 >= num2)
print(f"{num1} <= {num3}:", num1 <= num3)


# 6. Operadores Lógicos 0043 (python_operators_logical.asp)

# Ejemplo 1: Operador AND (devuelve True si ambas condiciones son verdaderas)
edad_persona = 22
tiene_licencia = True
puede_conducir = edad_persona >= 18 and tiene_licencia

print("\n--- 6. Operadores Lógicos - Ejemplo 1 (AND) ---")
print("¿Puede conducir?:", puede_conducir)

# Ejemplo 2: Operador OR (devuelve True si al menos una condición es verdadera)
es_fin_de_semana = False
es_feriado = True
hay_descanso = es_fin_de_semana or es_feriado

print("\n--- 6. Operadores Lógicos - Ejemplo 2 (OR) ---")
print("¿Hay descanso?:", hay_descanso)

# Ejemplo 3: Operador NOT (invierte el resultado booleano)
usuario_bloqueado = False
permiso_acceso = not usuario_bloqueado

print("\n--- 6. Operadores Lógicos - Ejemplo 3 (NOT) ---")
print("¿Tiene permiso de acceso?:", permiso_acceso)

print("Trabajo realizado por Sebastian Farfan NC = 0043")