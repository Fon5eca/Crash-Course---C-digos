import json




def encontrar_archivo(file_name):
    with open(file_name) as f:
        return json.load(f)
    
def guardar_num():
    num_fav = input("Por favor, ingresa tu número favorito para recordarlo (s para salir) ")
    if num_fav == "s":
        return "s"
    else:
        with open("num_fav.json", "a") as f:
            json.dump(num_fav, f)

def adivinar(num):
    print("Tu número favorito es...")
    print(f"¡{num}!")


try:
    num = encontrar_archivo("num_fav.json")

except FileNotFoundError:
    if guardar_num() == "s":
        pass

else:
    adivinar(num)