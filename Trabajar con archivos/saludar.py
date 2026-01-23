import json


def verif_usr(usr_file):
    with open(usr_file) as f:
        return json.load(f)

def saludar(name):
    print(f"¡Hola, {name}!")


try:
    user = verif_usr("users.json")

except FileNotFoundError:
    user = input("Ingresa tu nombre para recordarlo, por favor: ")
    with open("users.json", "a") as f:
        json.dump(user, f)
else:
    saludar(user)