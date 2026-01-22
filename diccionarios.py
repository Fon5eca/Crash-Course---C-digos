# Adriana ={
#     "Nombre": "Adriana",
#     "Apellido": "Blanco",
#     "Edad": 38,
#     "Ciudad": "Quepos",
# }

# print(Adriana["Nombre"])
# print(Adriana["Apellido"])
# print(Adriana["Edad"])
# print(Adriana["Ciudad"])


# num_fav = {
#     "Adrián": 8,
#     "Adriana": 2,
#     "Deisler": 5,
#     "Paola": 27,
#     "Magaly": 20
# }

# print("Adriana:", num_fav["Adriana"])
# print("Adrián:", num_fav["Adrián"])
# print("Deisler:", num_fav["Deisler"])
# print("Paola:", num_fav["Paola"])
# print("Magaly:", num_fav["Magaly"])


# diccionario_informatico = {
#     "Framework": "Piezas de código libres que se pueden reutilizar",
#     "Snippets": "Abreviaturas de comandos que hacen más internamente",
#     "Snapshot": "Vistazo instantáneo del estado de un programa",
#     "Metadatos": "Datos acerca de un producto (programa, app, etc).",
#     "Built-in": "Que lo trae por defecto",
#     "Lazy evaluation": "Técnica que usan los generadores y range, que se basa en que no almacena un elemento hasta que este se use.",
#     "Generadores": "Tipo especial de iterable que permite almacenar grandes cantidades de datos eficientemente.",
#     "Iterable": "Cualquier objeto que permite devolver cada uno de sus elementos uno por uno.",
#     "Métodos Dunder": "Son métodos que sirven para la sobrecarga de operadores o para implementar comportamientos. Sirven para definir o redefinir qué hacen ciertas acciones en un programa.",
# }

# for palabra, definicion in diccionario_informatico.items():
#     print(f"{palabra}: {definicion}")



# rios = {
#     "Amazonas": "Brazil",
#     "Nilo": "Egipto",
#     "Gallega": "Costa Rica",
# }

# for rio, pais in rios.items():
#     print(f"{rio} se ubica en {pais}")

# for rio in rios.keys():
#     print(rio)

# for pais in rios.values():
#     print(pais)



# encuesta = {
#     "Santiago": "Python",
#     "Elizabeth": "Java",
#     "Mario": "Java Script",
#     "Sarah": "Python",
#     "Estefano": "Python",
#     "Julieta": "C++",
# }

# personas = ["Julieta", "Matías", "Estefano", "Andrés", "Carlos", "María"]

# for persona in personas:
#     if persona in encuesta.keys():
#         print(f"Gracias por votar, {persona}")
#     else:
#         print(f"Recuerda votar, {persona}")



# Adriana = {
#     "Nombre": "Adriana",
#     "Apellido": "Blanco",
#     "Edad": 38,
#     "Ciudad": "Quepos",
# }

# Deisler = {
#     "Nombre": "Deisler",
#     "Apellido": "Fonseca",
#     "Edad": 16,
#     "Ciudad": "Quepos",
# }

# Adrián = {
#     "Nombre": "Adrián",
#     "Apellido": "Zapata",
#     "Edad": 9,
#     "Ciudad": "Quepos",
# }

# personas = [Adriana, Deisler, Adrián]

# for persona in personas:
#     print(f"{persona["Nombre"]} {persona["Apellido"]} tiene {persona["Edad"]} años y vive en {persona["Ciudad"]}.")



# Sami = {
#     "Nombre": "Sami",
#     "Tipo": "Perro",
#     "Dueño": "Roberto",
# }

# Nero = {
#     "Nombre": "Nero",
#     "Tipo": "Perro",
#     "Dueño": "Royner",
# }

# Pepe = {
#     "Nombre": "Pepe",
#     "Tipo": "Loro",
#     "Dueño": "Zenón",
# }

# Nemo = {
#     "Nombre": "Nemo",
#     "Tipo": "Pez",
#     "Dueño": "Disney",
# }

# animales = [Sami, Nero, Pepe, Nemo]

# for animal in animales:
#     print(f"{animal["Nombre"]} es un {animal["Tipo"].lower()} y su dueño es {animal["Dueño"]}.")



# lugares = {
#     "Deisler": ["Japón", "Islandia", "Grecia"],
#     "Adrián": ["Japón", "Chile"],
#     "Roberto": ["República Dominicana"],
# }

# for persona, lugar in lugares.items():
#     print(f"{persona} quiere ir a:")
#     for pais in lugar:
#         print("\t" + pais)



# num_fav = {
#     "Adrián": [8],
#     "Adriana": [2, 5, 8],
#     "Deisler": [5,8,7,2,24],
#     "Paola": [27],
#     "Magaly": [20],
# }

# for persona, nums in num_fav.items():
#     if len(nums) != 1:
#         print(f"Los números favoritos de {persona} son:")
#         for num in nums:
#             print(f"\t{num}")
#     else:
#         print(f"El número favorito de {persona} es:")
#         print(f"\t{nums[0]}")



# ciudades = {
#     "Quepos": {
#         "País": "Costa Rica",
#         "Población": 26_500,
#         "Dato": "Contiene al parque más visitado de Costa Rica",
#     },
#     "Nicoya": {
#         "País": "Costa Rica",
#         "Población":57_000,
#         "Dato":"Es una de las 5 regiones azules del mundo",
#     },
#     "Z**": {
#         "País": "Japón",
#         "Población":15_000,
#         "Dato":"Aparece en 'La muralla y sus muros inciertos'",
#     },
# }

# for ciudad, datos in ciudades.items():
#     print(f"Los datos acerca de {ciudad} son:")
#     for dato, valor in datos.items():
#         print(f"{dato}: {valor}")


# clientes = {
#     "Bareta": 1_200_000,
#     "Mony Rico": 1_000_000,
#     "Henry": 2_000_000,
#     "Pichi": 120_000,
# }

# valor_max = max(clientes.values())

# for cliente, ganancia in clientes.items():
#     if ganancia == valor_max:
#         print(f"El cliente que más ganancias generó durante el mes es {cliente}, con una ganancia total de {ganancia}")