"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error."""
num1 = float(input("Escribe el primer numero: "))
num2 = float(input("Escribe el segundo numero: "))
if num2 == 0:
    print("Error")
else:
    div = num1 / num2 
    print(div)