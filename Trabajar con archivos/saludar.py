import json


def verif_usr(usr_file):
    ''' Abrir el archivo si existe, leerlo y devolver lo que haya dentro. '''
    with open(usr_file) as f:
        return json.load(f)

def saludar(name):
    print(f"¡Hola, {name}!")

def almacenar_user():
    with open("users.json", "a") as f:
        user = input("Ingresa tu nombre para recordarlo, por favor: ")
        json.dump(user, f)
    print("¡Excelente, ahora podremos recordar tu nombre!")

def updt_usr():
    new_user = input("Por favor, ingresa el nuevo nombre de usuario ")
    with open("users.json", "w") as f:
        json.dump(new_user, f)
    print("¡Usuario actualizado!")


try:
    user = verif_usr("users.json")

except FileNotFoundError:
    almacenar_user()

else:
    respuesta = input(f"¿Tu usuario es {user}? (s/n) ")
    
    if respuesta == "n":
        updt_usr()
    else:
        saludar(user)