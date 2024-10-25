"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo que tenga tantas líneas como el número introducido, como el triángulo de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""
num = int(input("Escriba un numero entero: "))

for i in range(1, num + 1):
    for j in range(i, 0, - 1):
        print(2 * j - 1, end="")
    print()