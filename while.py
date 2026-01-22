# mensaje = input("Escriba la palabra que será repetida o escriba 'salir' para salir del juego: ")

# while mensaje != "salir":
#     print(mensaje)
#     mensaje = input("Escriba la palabra que será repetida o escriba 'salir' para salir del juego: ")



# toppings_disponibles = ["Queso Extra", "Salsa De Tomate", "Hongos", "Frutas"]

# while True:
#     topping = input("Ingresa el tipo de topping que quieres o escribe 'salir' para salir: ").title()

#     if topping == "Salir":
#         break

#     elif topping not in toppings_disponibles:
#         print(f"Lo siento, no tenemos {topping}")
#         continue

#     else:
#         print(f"¡Añadiendo {topping}!")



# personas = 0
# estado = "activo"

# while 15 > personas:
#     edad = int(input("¿Cuál es tu edad? (Presiona '-1' para salir) "))

#     if edad == -1:
#         estado = "inactivo"

#     elif 3 > edad:
#         print("¡Tu entrada es gratis!")
#     elif 12 > edad:
#         print("Pagas 10 dólares")
#     else:
#         print("Tu entrada cuesta 15 dólares")

#     if estado == "inactivo":
#         break
    
#     personas += 1

# while True:
#     print("Deisler es un guapo >:)")



# ordenes_sandwich = ["Sandwich de atún", "Pastrami", "Sandwich de pan integral", "Pastrami", "Sandwich de mortadela", "Pastrami"]
# sandwiches_listos = []

# print("Lo siento, pero nos quedamos sin pastrami")
# while "Pastrami" in ordenes_sandwich:
#     ordenes_sandwich.remove("Pastrami")

# while ordenes_sandwich:
#     preparando = ordenes_sandwich.pop()
#     sandwiches_listos.append(preparando)
#     print(f"!Preparando {preparando.lower()}!")

# print("Estos son los sandwiches preparados:")

# for sandwich in sandwiches_listos:
#     print(sandwich)



respuestas = {

}

while True:
    nombre = input("¿Cuál es tu nombre? ")
    lugar = input("¿Qué lugar te gustaría visitar? ")
    respuestas[nombre] = lugar

    respuesta = input("¿Falta alguien más? (Sí / No) ")
    if respuesta == "No":
        break

for nombre, lugar in respuestas.items():
    print(f"{nombre} quiere ir a {lugar}")