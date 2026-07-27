#while True:
#    print("Estoy atrapado dentro de un bucle.")
'''
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)'''
"""
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
 
i = 0
while i < 100:
    # do_something()
    i += 1
    print(i)

for i in range(2, 8):
    print("El valor de i es", i)

#El tercer argumento es un incremento 
for i in range(2, 8, 3):
    print("El valor de i es", i)
"""
for i in range(1, 1):
    print("El valor de i es", i)
for i in range(2, 1):
    print("El valor de i es", i)

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")