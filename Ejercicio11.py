"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última."""
x = input("Escribe la palabra: ")
for letra in x[::-1]:
    print(letra)