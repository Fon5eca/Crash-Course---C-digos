class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")

user1 = Usuario(nombre, apellido, edad)

with open("usuarios.txt", "a") as usuarios:
    usuarios.write(user1.nombre)