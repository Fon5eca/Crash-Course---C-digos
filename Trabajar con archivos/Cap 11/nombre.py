import ejemplo

print("¡Bienvenido! En cada pregunta puedes poner 'q' para salir")

while True:
    nombre = input("Por favor, ingresa tu nombre: ")
    if nombre == "q":
        break
    apellido = input("Ahora, pon tu apellido: ")
    if apellido == "q":
        break
    opcion = input("¿Deseas agregar un segundo nombre? (s/n): ")
    if opcion == "q":
        break
    elif opcion == "n":
        print(ejemplo.nombre(nombre, apellido))
    else:
        s_n = input("Bien, agrega tu segundo nombre: ")
        print(ejemplo.nombre(nombre, apellido, s_n))