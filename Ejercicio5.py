"""Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""
nombre = input("Escriba su nombre: ")
sexo = input("Esciba su sexo: ")
if sexo.lower() == "mujer" and nombre[0].lower() < "m":
    print("Gryffindor")
elif sexo.lower() == "hombre" and nombre[0].lower() > "m":
    print("Gryffindor")
else:
    print("Slytheryn")