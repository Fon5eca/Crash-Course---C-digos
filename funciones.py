# def mostrar_mensaje(tema):
#     print(f"En este capítulo estoy aprendiendo el siguiente tema: {tema}")

# mostrar_mensaje("Funciones")



# def libro_fav(titulo_libro):
#     print(f"Uno de mis libros favoritos es {titulo_libro.title()}")

# libro_fav("La ciudad y sus muros inciertos")



# def hacer_camisa(talla = "L", mensaje = "Amo Python"):
#     print(f"El pedido es de una camisa de talla '{talla}' y que tenga impreso el mensaje '{mensaje}'")

# hacer_camisa("M", "Te amo mamá")
# hacer_camisa(talla = "L", mensaje = "Te amo papá")
# hacer_camisa()
# hacer_camisa("M")



# def describe_ciudad(ciudad, pais = "Costa Rica"):
#     print(f"{ciudad.title()} queda en {pais.title()}")

# describe_ciudad("Quepos")
# describe_ciudad("Caracas", "Venezuela")
# describe_ciudad(ciudad = "Santiago", pais = "Chile")


# def datos_de_persona(primer_nombre, segundo_nombre, edad, pais = None):
#     dic_datos = {
#         "Primer nombre": primer_nombre,
#         "Segundo nombre": segundo_nombre,
#         "Edad": edad
#     }

#     if pais:
#         dic_datos["País"] = pais
    
#     return dic_datos

# print(datos_de_persona("Deisler", "Neftali", 16, "Costa Rica"))



# def ciudad_pais(ciudad, pais):
#     return f"{ciudad.title()}, {pais.title()}"

# while True:
#     salir = input("¿Quieres seguir? (Sí/No) " )
#     if salir == "No":
#         break

#     ciudad = input("Por favor, introduce el nombre de la ciudad: ")
#     pais = input("Ahora, introduce el país al que pertenece: ")

#     print(ciudad_pais(ciudad, pais))



# def album_musical(artista, nombre_del_album, cant_canciones_album = None):
#     datos_album = {
#         "Artista": artista,
#         "Nombre del álbum": nombre_del_album,
#     }

#     if cant_canciones_album:
#         datos_album["Cantidad de canciones del álbum"] = cant_canciones_album

#     return datos_album

# while True:
#     salir = input("¿Deseas salir? (Sí/No) ")
#     if salir == "Sí":
#         break

#     artista = input("Por favor, introduce el nombre del artista: ")
#     album = input("Ahora, introduce el nombre de su álbum: ")

#     verificar = input("¿Quieres añadir la cantidad de canciones que tiene el álbum? (Sí/No) ")
#     if verificar == "Sí":
#         cantidad_canciones = input("Introduce la cantidad de canciones: ")

#         print(album_musical(artista, album, cantidad_canciones))

#     else:
#         print(album_musical(artista, album))



# mensajaes_por_enviar = ["Tú puedes", "Te amo", "Sigue así"]
# mensajes_enviados = []

# def mostrar_mensaje(mensaje):
#     print(f"El siguiente mensaje se está imprimiendo: '{mensaje}'")

# def mover_elemento(inicio, final):
#     while inicio:
#         elemento = inicio.pop()
#         final.append(elemento)
#         mostrar_mensaje(elemento)

# mover_elemento(mensajaes_por_enviar[:], mensajes_enviados)

# print(mensajaes_por_enviar)
# print(mensajes_enviados)



# def haciendo_sandwich(*ingredientes):
#     print("Estos son los ingredientes de tu sandwich:")
#     for ingrediente in ingredientes:
#         print(f"\t-{ingrediente}")

# haciendo_sandwich("Salsa de tomate", "Extra queso", "Mortadela")
# haciendo_sandwich("Frijoles", "Arroz")
# haciendo_sandwich("Doble pan")



# def crear_perfil(**datos):
#     print(datos)

# crear_perfil(Edad = 16, Estatura = "190 cm", Primer_nombre = "Deisler", Apellido = "Fonseca", Peso = "60 kg")



# def caracteristicas_carro(Empresa, Modelo, **extras):
#     extras["Empresa"] = Empresa
#     extras["Modelo"] = Modelo
#     print(extras)

# caracteristicas_carro("Mercedes-Benz Group AG", "Mercedes-AMG G63", Color = "Azul oscuro", Precio = "$200 000")