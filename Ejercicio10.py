"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""
contraseña = "1234"
while True:
    contr = input("Escribe tu contraseña: ")
    if contr == contraseña:
        print("Contarseña correcta")
        break
    else:
        print("Contraseña incorrecta")