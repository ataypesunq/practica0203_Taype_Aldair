"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""
while True:
    x = input("Escribe lo que sea o escribe `salir`: ")
    if x.lower() == "salir":
        break
    print(x)