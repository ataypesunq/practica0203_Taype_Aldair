"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""
frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
num_letras = ""
for x in frase.lower():
    if x == letra.lower():
        num_letras += x
cont_num_veces = len(num_letras)
print(f"La {letra} aparece {cont_num_veces}.")