"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""
contraseña = input("Crea la contraseña: ")
ped_contras = input("Escribe la contraseña: ")
if ped_contras.lower() == contraseña.lower() :
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")